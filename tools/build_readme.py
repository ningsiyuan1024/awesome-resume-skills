"""Build the catalog tables without copying upstream skill instructions."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'))
entries=data['entries']
def table(rows):
    lines=['| 项目 | 适合做什么 | 输出 | 环境与使用限制 | 中文实测 |','| --- | --- | --- | --- | --- |']
    for e in rows:
        url=f"https://github.com/{e['repo']}"
        skill=f"https://github.com/{e['repo']}/blob/main/{e['path']}"
        refs=f'[Skill]({skill})'
        if e.get('extra_paths'):refs+=' · [Canvas](https://github.com/'+e['repo']+'/blob/main/'+e['extra_paths'][0]+')'
        test=e.get('test_result')
        tested=f"[{test['status']}]({test['report']})<br>{test['summary']}" if test else '未实测'
        lines.append(f"| **[{e['id']}]({url})**<br>{refs} | {e['summary']}<br>语言：{e['languages']} | {' / '.join(e['outputs'])} | {e['limits']} | {tested} |")
    return '\n'.join(lines)

layout=[e for e in entries if e['status']=='listed' and e['category']=='layout']
content=[e for e in entries if e['status']=='listed' and e['category']=='content']
watch=[e for e in entries if e['status']=='watch']
head=f'''# Awesome Resume Skills

面向中文求职者的简历 Agent Skills 清单：中文排版、Word/PDF 渲染、成果表达、JD 适配与交付检查。

A Chinese-first, evidence-linked directory of resume agent skills, with practical notes on typography, editable formats and runtime requirements.

**最近核查：{data['checked_on']}。** 收录 {len(layout)} 个排版与交付项目、{len(content)} 个内容优化项目，另列 {len(watch)} 个待评估项目。全部 13 个项目已做固定版本检查：9 个排版项目生成中文基础样例，3 个内容工作流完成单次演练，1 个项目依赖阻塞；部分样例存在保真或分页缺陷，不能统一标成通过。见 [中文实测报告](tests/2026-11-14/README.md)。这不是招聘效果认证、安全审计或完整自主 Agent 评测。

## 快速选择

- **中文技术简历 PDF 首选**：[RenderCV](https://github.com/rendercv/rendercv-skill)；六主题样例通过，需设置中文字体，长文开启跨页。
- **必须交付可编辑 Word**：优先 [JSON-Resume](https://github.com/Eric-Zhou-0302/JSON-Resume)，中文 DOCX 和 Word 导出 PDF 已测；另一项目 resume-layout-skill 存在输入语法与教育地点默认值问题。
- **想比较中文模板**：[cosen1024/resume-builder-skill](https://github.com/cosen1024/resume-builder-skill) 的五模板有通过路线；Windows 原生依赖需补齐，WSL 必须配置 CJK 字体。
- **现有正文只换排版**：看 [ResumeMD](https://github.com/beholder91/resume-md-skill)；原生 Windows 当前不在它的支持范围。
- **希望自己微调字号和间距**：看 [Chasen-Liao 的 resume-canvas](https://github.com/Chasen-Liao/resume-skills/tree/main/skills/resume-canvas)，仅适配其内置视觉模板。
- **内容像流水账**：先看内容优化类，再交给排版工具。没有收益数字时保留可观察产物，不补造百分比。

## 目录

- [排版与文件交付](#排版与文件交付)
- [内容、成果与岗位适配](#内容成果与岗位适配)
- [待评估与适用限制](#待评估与适用限制)
- [相邻工具](#相邻工具)
- [中文社区发现记录](docs/community-sources.md)
- [中文实测报告与失败记录](tests/2026-11-14/README.md)
- [收录和核查标准](#收录和核查标准)
- [贡献条目](CONTRIBUTING.md)

## 排版与文件交付

'''
tail='''
## 相邻工具

以下是渲染器或模板库，不计入已收录 Skill 数量：

- [YAMLResume](https://github.com/yamlresume/yamlresume)：结构化内容与简历渲染生态，中文社区有作者分享。是否有可用 Skill、输出格式和版本以实际项目文档为准。
- [中文简历模板库](https://github.com/ql-link/drawoffer-chinese-resume-templates)：可用于比较中文简历的信息层级与视觉版式。模板数量和授权以仓库当前说明为准，本清单未运行模板。

## 中文社区发现记录

从 V2EX、LINUX DO 及中文项目文档反查作者仓库，详细来源见 [社区记录](docs/community-sources.md)。社区发帖、作者宣传、第三方使用反馈分别记录；点赞、收藏、评分和“ATS-friendly”标签均不作为获得面试的证据。

## 收录和核查标准

1. 核心条目必须有公开、可定位的 `SKILL.md`；普通简历网站、提示词列表和模板库另列。
2. 读取原始 Skill 入口和与能力相关的 README / 排版参考，记录输入、输出、语言与运行依赖。
3. 明确区分**文档已读、依赖安装、原脚本执行、模板适配渲染、中文样例验证、完整 Agent 工作流、真实求职反馈**。本轮实测范围逐项记录；内容类单次演练不能作为独立模型评测。
4. 不凭仓库名称推断功能；不凭一个测试成功宣称全平台、所有字体或 ATS 均可用。
5. 不把 Skill 内“必须一页”、使用照片或强动词等个人规则当作所有求职者的固定要求。事实与个人归因应优先于模板。
6. 排版核查应包含实际页数、文本可提取、字体、裁切/重叠和阅读顺序。Word 成功保存不等于 PDF 正确渲染。
7. 本仓库只发布公共资源链接与原创概述，不收集真实简历、联系方式、客户资料或内部代码。

### 安装和使用

先进入项目链接查看当前安装说明。安装 Skill 与安装渲染器是两件事；包含公共脚本、字体和模板的项目应按上游目录完整安装。某些项目的 Skill 名称相同，安装前注意目标目录冲突。

安装不自动授权改写事实、上传简历、投递或联系招聘方。推荐为“忠实排版”明确指定输入稿；为“成果改写”保留原始事实与作者确认记录。不要为了凑一页把字号压到难以阅读，也不要隐藏溢出内容。

## 数据与维护

- [catalog.json](catalog.json)：条目、Skill 路径、输出格式、来源和限制。
- [测试输入、固定版本和结构化结果](tests/2026-11-14/)：完全虚构的中文样例，保留失败与适配条件。
- `python tools/build_readme.py`：从清单重建本页。
- `python tools/validate_catalog.py`：检查重复条目、必填字段、源链接和 README 一致性；不执行上游代码，也不构成在线链接可用性测试。
- 核查时间是本项目阅读日期；上游默认分支可能变化。新增实跑结果须记录版本、操作系统、样本和产物检查，不覆盖失败记录。

## License

本仓库原创目录、说明与维护脚本使用 [MIT License](LICENSE)。链接项目、字体和模板各自保留原授权；收录不授予其代码或素材的再分发权。
'''
text=head+table(layout)+'\n\n## 内容、成果与岗位适配\n\n'+table(content)+'\n\n## 待评估与适用限制\n\n下面项目有明确能力线索，但存在适配或使用规则问题；列出用于比较，不作为开箱即用推荐。\n\n'+table(watch)+'\n'+tail
(ROOT/'README.md').write_text(text,encoding='utf-8',newline='\n')
print(f'Generated README: {len(layout)} layout, {len(content)} content, {len(watch)} watch.')
