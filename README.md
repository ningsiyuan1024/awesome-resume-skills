# Awesome Resume Skills

面向中文求职者的简历 Agent Skills 清单：中文排版、Word/PDF 渲染、成果表达、JD 适配与交付检查。

A Chinese-first, evidence-linked directory of resume agent skills, with practical notes on typography, editable formats and runtime requirements.

**最近核查：2026-11-14。** 收录 6 个排版与交付项目、3 个内容优化项目，另列 4 个待评估项目。全部 13 个项目已做固定版本检查：9 个排版项目生成中文基础样例，3 个内容工作流完成单次演练，1 个项目依赖阻塞；部分样例存在保真或分页缺陷，不能统一标成通过。见 [中文实测报告](tests/2026-11-14/README.md)。这不是招聘效果认证、安全审计或完整自主 Agent 评测。

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

| 项目 | 适合做什么 | 输出 | 环境与使用限制 | 中文实测 |
| --- | --- | --- | --- | --- |
| **[rendercv](https://github.com/rendercv/rendercv-skill)**<br>[Skill](https://github.com/rendercv/rendercv-skill/blob/main/skills/rendercv/SKILL.md) | 官方维护的 Typst 简历排版入口，提供工程、Harvard 等六套主题及字体、边距、间距配置。<br>语言：含中文语言配置 | PDF / PNG / HTML / Markdown / YAML | 需要 RenderCV 运行时；未列出 DOCX 输出。中文字体与实际分页需渲染确认。 | [baseline_pass_with_configuration](tests/2026-11-14/README.md)<br>推荐 PDF 排版；六主题中文一页通过。需配置中文字体；40 条长文默认设置裁字，开启章节和条目跨页后两页通过。 |
| **[cosen-resume-builder](https://github.com/cosen1024/resume-builder-skill)**<br>[Skill](https://github.com/cosen1024/resume-builder-skill/blob/main/resume_skill/SKILL.md) | 中文优先，提供 compact、classic、modern、timeline、minimal 五套模板，使用 WeasyPrint 本地渲染。<br>语言：中文、英文、中英双语 | PDF / HTML / Markdown | 需要 Python 与 WeasyPrint 系统依赖。包含内容润色流程，只排版时应明确保留原文；原规则中的强动词不能扩大本人职责。 | [conditional](tests/2026-11-14/README.md)<br>五模板 HTML + Edge 输出通过；Windows 原生 WeasyPrint 缺 DLL。WSL 补齐中文字体与 fontconfig 后 compact 通过；缺字体首次输出中文丢失。 |
| **[json-resume-docx](https://github.com/Eric-Zhou-0302/JSON-Resume)**<br>[Skill](https://github.com/Eric-Zhou-0302/JSON-Resume/blob/main/SKILL.md) | 从结构化 JSON 生成 Word 简历，区分忠实渲染与内容创作模式，要求实际导出和逐页检查。<br>语言：中文及英文混排 | DOCX / PDF / JSON | PDF 导出依赖 Windows/macOS 的 Microsoft Word；在线编辑器与本地 CLI 的数据路径不同。项目名不代表兼容 jsonresume.org 标准。 | [baseline_pass_with_configuration](tests/2026-11-14/README.md)<br>推荐 Word；按其 JSON 契约适配后，原 CLI 生成 DOCX 并通过 Word 导出一页 PDF。标签联系人需显式 href:null。 |
| **[resume-docx](https://github.com/Denis-Tang/resume-layout-skill)**<br>[Skill](https://github.com/Denis-Tang/resume-layout-skill/blob/main/SKILL.md) | Markdown 源文件与 Word 双向维护，含模板自举、Word 页数检查及预览流程。<br>语言：中文 | DOCX / PNG / Markdown | 精确页数依赖 Word；Python 页数检查是估算。源规则有严格的一页及固定版式约束，具体任务以用户要求为准。 专用 Markdown 语法需适配；原脚本会把个人所在地补进教育所在地，严格保真有缺陷。 专用 Markdown 语法需适配；原脚本会把个人所在地补进教育所在地，严格保真有缺陷。 | [partial](tests/2026-11-14/README.md)<br>适配专用 Markdown 语法后文字保留；普通语法会漏联系信息和教育。原脚本把个人所在地补进学校所在地，严格保真不通过。 |
| **[resumemd](https://github.com/beholder91/resume-md-skill)**<br>[Skill](https://github.com/beholder91/resume-md-skill/blob/main/plugins/resume-md/skills/resume-md/SKILL.md) | 保真转换与确定性本地排版，关注字体嵌入、可提取文本和自然分页，不为排版主动改写内容。<br>语言：中文优先，也支持英文 | PDF / Markdown | 上游 README 声明支持 macOS、Linux、WSL，暂不支持原生 Windows、多栏或头像；不强制一页。 | [baseline_pass_on_supported_platform](tests/2026-11-14/README.md)<br>WSL Ubuntu 原 CLI 输出中文一页，Noto Sans SC 字体下载成功；原生 Windows 不在上游支持范围。 |
| **[chasen-resume-skills](https://github.com/Chasen-Liao/resume-skills)**<br>[Skill](https://github.com/Chasen-Liao/resume-skills/blob/main/skills/resume-builder/SKILL.md) · [Canvas](https://github.com/Chasen-Liao/resume-skills/blob/main/skills/resume-canvas/SKILL.md) | 母版构建与岗位定制工作流，提供视觉版、单栏版，以及本地 Canvas 字号和间距微调。<br>语言：中文工作流 | HTML / PDF / YAML | Canvas 只适配内置视觉模板，不适用于 ATS-safe 或任意外部 HTML；需完整渲染环境，不生成 DOCX。 | [conditional_visual_issue](tests/2026-11-14/README.md)<br>Edge 适配后原渲染器通过；Canvas 编辑、保存、读回及重导出已操作验证。短稿出现大段纵向留白，需调布局。默认 Chromium 下载在本次环境超时。 |

## 内容、成果与岗位适配

| 项目 | 适合做什么 | 输出 | 环境与使用限制 | 中文实测 |
| --- | --- | --- | --- | --- |
| **[resume-optimizer](https://github.com/wyh0626/resume-optimizer)**<br>[Skill](https://github.com/wyh0626/resume-optimizer/blob/main/SKILL.md) | 审计职责型表述，围绕成果、交付物和业务价值改写，并结合 JD 调整重点。<br>语言：中文 | 诊断 / 改写草稿 / 行动清单 | 主要是内容工作流，不能当作确定性排版器或面试率保证；缺失指标仍需用户事实。 | [single_session_only](tests/2026-11-14/README.md)<br>按上游流程做一次中文样例审计，保留团队归属与未测量项；非独立或重复模型评测，无排版器验收。 |
| **[resume-coach](https://github.com/leemysw/skills)**<br>[Skill](https://github.com/leemysw/skills/blob/main/resume-coach/SKILL.md) | 从招聘阅读视角分析定位、成果叙事和 JD 匹配，配套解析 PDF/DOCX 等文件。<br>语言：中文 | 评分卡 / 诊断 / 改写草稿 | 评分是提示词定义的主观检查，未经招聘结果校准；不属于模板排版工具。 实跑发现 DOCX 表格文字被跳过；优先输入已核对的 PDF / Markdown。 实跑发现 DOCX 表格文字被跳过；优先输入已核对的 PDF / Markdown。 | [partial_parser_and_single_session](tests/2026-11-14/README.md)<br>中文诊断单次演练完成；MD/PDF 解析保留检查项。DOCX 解析只读普通段落，漏掉表格中的公司、学校和项目标题，不可直接信任诊断。 |
| **[repo-to-resume-tailor](https://github.com/Ssabby1/repo-to-resume-tailor)**<br>[Skill](https://github.com/Ssabby1/repo-to-resume-tailor/blob/main/repo-to-resume-tailor/SKILL.md) | 从代码、配置和架构材料提炼项目描述，按岗位方向或具体 JD 选择高信号证据。<br>语言：中文及英文说明 | 证据分析 / 项目经历正文 | 仓库功能不等于个人贡献，代码存在不证明业务收益；内部项目应留在授权的本地环境。 | [single_session_only](tests/2026-11-14/README.md)<br>用虚构仓库做一次中文证据演练，区分本人函数与参考模板；不证明真实履历收益或重复执行质量。 |

## 待评估与适用限制

下面项目有明确能力线索，但存在适配或使用规则问题；列出用于比较，不作为开箱即用推荐。

| 项目 | 适合做什么 | 输出 | 环境与使用限制 | 中文实测 |
| --- | --- | --- | --- | --- |
| **[resume-builder-cn](https://github.com/LittleDrunkWang/resume-builder-cn)**<br>[Skill](https://github.com/LittleDrunkWang/resume-builder-cn/blob/main/SKILL.md) | 提供单栏、研发成果型、侧栏和学术版式规则，含短词断行与可编辑 HTML 参数。<br>语言：中文、英文、双语 | HTML / Markdown / PDF | 入口 YAML 解析有效；本轮只验证内置可编辑模板 + Edge 导出，完整内容与研究流程未执行。 | [template_only](tests/2026-11-14/README.md)<br>入口 YAML 有效。上游可编辑模板填入同一虚构样例后用 Edge 导出通过；没有执行完整访谈、岗位研究及其原导出脚本。 |
| **[init-resume-builder](https://github.com/INIT1996/resume-builder)**<br>[Skill](https://github.com/INIT1996/resume-builder/blob/main/SKILL.md) | 中文优先的 HTML 简历生成与分页规则，强调保留事实与可编辑交付。<br>语言：中文优先 | HTML | 入口 YAML 有效；中文单页模板通过，多块长文示例分页会隐藏内容。PDF 不是默认交付物，需单独导出并查页边。 | [baseline_only_stress_fail](tests/2026-11-14/README.md)<br>入口 YAML 有效。样例模板单页通过；多块长文示例分页生成 5 页，7 个压力编号的完整正文不可提取，页面边缘可见裁切。 |
| **[resume-md2pdf](https://github.com/HduSy/resume-md2pdf)**<br>[Skill](https://github.com/HduSy/resume-md2pdf/blob/main/SKILL.md) | 忠于 Markdown 原文设计视觉主题，用 Chromium 导出 A4 PDF。<br>语言：中文或纯英文 | HTML / PDF | 上游明确不做中英混排，包含浏览器预览和确认环节；技术词密集的中文简历需先验证。 | [conditional](tests/2026-11-14/README.md)<br>上游建 HTML 和导出脚本使用 Edge，中文技术词混排样例及 40 条长文通过。上游仍明确不支持混排，不将一次成功扩展为通用支持。 |
| **[resume-factory](https://github.com/hyf020908/resume-factory)**<br>[Skill](https://github.com/hyf020908/resume-factory/blob/main/SKILL.md) | 十套 LaTeX 风格，强调内容保真、编译与版面检查。<br>语言：可指定目标语言 | PDF / LaTeX | 当前规则要求照片，并允许为强制一页把正文压到 5.5pt 甚至更小；不宜不加判断地用于正式求职简历。 | [blocked_environment](tests/2026-11-14/README.md)<br>真实上游模板的 XeLaTeX 编译探针缺 TikZ shadows.blur，未生成 PDF；不是完整中文样例通过。未为测试安装全局 TeX 包。 |

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
