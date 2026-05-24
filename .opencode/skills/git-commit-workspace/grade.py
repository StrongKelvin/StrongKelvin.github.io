import json, os, re, glob

workspace = os.path.dirname(os.path.abspath(__file__))
iteration = os.path.join(workspace, "iteration-1")

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""

# Extract short name from eval dir (e.g., "eval-1-fix-header-navigation" -> "fix-header-navigation")
def short_name(eval_dir):
    parts = eval_dir.split("-", 2)
    return parts[2] if len(parts) > 2 else eval_dir

for eval_dir in sorted(os.listdir(iteration)):
    eval_path = os.path.join(iteration, eval_dir)
    if not os.path.isdir(eval_path): continue
    meta_path = os.path.join(eval_path, "eval_metadata.json")
    if not os.path.exists(meta_path): continue

    metadata = json.load(open(meta_path, "r", encoding="utf-8"))
    assertions = metadata.get("assertions", [])
    sname = short_name(eval_dir)

    for config in ["with_skill", "without_skill"]:
        outputs_dir = os.path.join(eval_path, config, "outputs")
        if not os.path.exists(outputs_dir): continue

        msg = read_file(os.path.join(outputs_dir, "proposed-commit-message.txt"))
        interaction = read_file(os.path.join(outputs_dir, "interaction.txt"))
        lines = msg.strip().split("\n") if msg else []
        title = lines[0] if lines else ""

        expectations = []
        pc, fc = 0, 0

        for a in assertions:
            name = a["name"]
            passed = False
            evidence = ""

            if name == "bilingual-format":
                has_en = bool(re.match(r'^[a-z]+(\([^)]+\))?:\s', title))
                body = "\n".join(lines[2:]) if len(lines) >= 3 else ""
                has_zh = bool(re.search(r'[\u4e00-\u9fff]', body))
                passed = has_en and has_zh
                evidence = f"EN title: {has_en}, ZH body: {has_zh}"

            elif name == "conventional-commits":
                passed = bool(re.match(r'^[a-z]+(\([a-z0-9_-]+\))?:\s', title))
                evidence = f"Title: '{title}'" if passed else f"Bad format: '{title}'"

            elif name == "correct-scope":
                m = re.search(r'\(([a-z0-9_-]+)\)', title)
                expected = ""
                if "header" in eval_dir: expected = "header"
                elif "blog" in eval_dir: expected = "blog"
                actual = m.group(1) if m else "none"
                passed = actual == expected
                evidence = f"Expected '{expected}', got '{actual}'"

            elif name == "correct-type":
                m = re.match(r'^([a-z]+)', title)
                actual = m.group(1) if m else "none"
                if "header" in eval_dir: expected_list = ["feat"]
                elif "blog" in eval_dir: expected_list = ["feat", "docs"]
                else: expected_list = ["feat", "fix", "docs", "refactor"]
                passed = actual in expected_list
                evidence = f"Type '{actual}' in {expected_list}: {passed}"

            elif name == "appropriate-type":
                m = re.match(r'^([a-z]+)', title)
                actual = m.group(1) if m else "none"
                expected_list = ["chore", "refactor"]
                passed = actual in expected_list
                evidence = f"Type '{actual}' in {expected_list}: {passed}"

            elif name == "meaningful-body":
                body = "\n".join(lines[2:]) if len(lines) >= 3 else ""
                if "header" in eval_dir:
                    kws = ["Project", "導覽", "連結"]
                elif "blog" in eval_dir:
                    kws = ["Astro", "教學", "部落格", "文章"]
                else: kws = []
                found = [kw for kw in kws if kw in body]
                passed = len(found) >= 1
                evidence = f"Found keywords in body: {found}"

            elif name == "lists-both-changes":
                body = "\n".join(lines[2:]) if len(lines) >= 3 else ""
                has_style = any(w in body for w in ["樣式", "字體", "global.css", "style"])
                has_bug = any(w in body for w in ["bug", "formatDate", "日期", "驗證", "format"])
                passed = has_style and has_bug
                evidence = f"Style: {has_style}, Bug fix: {has_bug}"

            elif name == "respects-user-intent":
                split_phrases = ["拆分", "split commit", "split into", "分割", "separate commit"]
                passed = all(p not in interaction.lower() for p in split_phrases)
                evidence = "No commit splitting suggested" if passed else "Agent suggested splitting commits"

            else:
                evidence = "Unknown assertion"

            expectations.append({
                "text": a["description"],
                "passed": passed,
                "evidence": evidence
            })
            if passed: pc += 1
            else: fc += 1

        total = len(assertions)
        grading = {
            "expectations": expectations,
            "summary": {
                "passed": pc, "failed": fc, "total": total,
                "pass_rate": round(pc / total, 2) if total > 0 else 0
            },
            "execution_metrics": {},
            "claims": [],
            "eval_feedback": {"suggestions": [], "overall": "Auto-graded"}
        }

        gp = os.path.join(eval_path, config, "grading.json")
        with open(gp, "w", encoding="utf-8") as f:
            json.dump(grading, f, ensure_ascii=False, indent=2)
        print(f"{eval_dir}/{config}: {pc}/{total} passed ({grading['summary']['pass_rate']:.0%})")
