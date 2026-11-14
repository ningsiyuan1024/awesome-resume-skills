# 中文简历兼容性测试 · 2026-11-14

本轮对清单全部 13 个项目固定版本检查：9 个排版项目生成了保留中文的基础样例，3 个内容工作流做了本会话单次演练，1 个 LaTeX 项目被当前环境依赖阻塞。**生成文件不等于完整通过，也不等于原生 Windows 开箱即用。** 各条限制如下。

优先推荐 **RenderCV 生成 PDF**、**JSON-Resume 交付可编辑 Word**；能使用 WSL 时可选 ResumeMD。RenderCV 必须配置中文字体，长内容允许跨页。严格保真场景暂不推荐直接使用 resume-layout-skill 的默认教育地点处理。

## 测试输入与验收范围

- 一份完全虚构的中文技术简历：中文姓名、邮箱、学校、学历、日期、公司、三项目、9 条正文。人物、机构、履历与指标不对应真实候选人。
- 保留 `Qwen2.5-VL-3B-Instruct`、`84.9%`、`93%+`、MCP、iframe、merge-base 等中英混排与标点。
- 事实边界：固定 20 个任务的结果不能外推；团队 5 人日至 3 人日不能写成个人独立成果；未测量的时间收益不能补百分比；虚构 JD 的 Rust 要求不能变成已有技能。
- 检查实际 PDF 页数、A4、9 条正文、17 个身份与内容标记、替代字符、文本边界和中文字号，并查看页面图像。字号统计是含至少 8 个汉字的文本 span 的最小值，仅为参考。
- 长文测试额外增加 40 条，检查每个编号是否完整保留。长文仅覆盖 RenderCV、cosen compact 的 HTML 路线、Hdu、INIT 示例分页，不能声称全部模板均通过长文测试。
- 所有 13 个主入口 frontmatter 均能被 YAML 解析。此前对 LittleDrunk / INIT 入口格式的疑虑已解除；这不等于在所有 Agent 宿主中安装与调用均验收成功。

## 逐项结果

| 项目与固定版本 | 测试结论 | 实际范围与限制 |
| --- | --- | --- |
| [rendercv](https://github.com/rendercv/rendercv-skill/tree/fc14e727b2d4a36c612ef0989726bd18411218d7) | `baseline_pass_with_configuration` | 推荐 PDF 排版；六主题中文一页通过。需配置中文字体；40 条长文默认设置裁字，开启章节和条目跨页后两页通过。 |
| [cosen-resume-builder](https://github.com/cosen1024/resume-builder-skill/tree/a4bfa74bd72ef1a75fd9c02ac1e27dd353f6dde1) | `conditional` | 五模板 HTML + Edge 输出通过；Windows 原生 WeasyPrint 缺 DLL。WSL 补齐中文字体与 fontconfig 后 compact 通过；缺字体首次输出中文丢失。 |
| [json-resume-docx](https://github.com/Eric-Zhou-0302/JSON-Resume/tree/9ca9ada33c927dadaf8e483c2269165847830e85) | `baseline_pass_with_configuration` | 推荐 Word；按其 JSON 契约适配后，原 CLI 生成 DOCX 并通过 Word 导出一页 PDF。标签联系人需显式 href:null。 |
| [resume-docx](https://github.com/Denis-Tang/resume-layout-skill/tree/3cdde8a109b8bc83fae66ed69d4b910385e2fe12) | `partial` | 适配专用 Markdown 语法后文字保留；普通语法会漏联系信息和教育。原脚本把个人所在地补进学校所在地，严格保真不通过。 |
| [resumemd](https://github.com/beholder91/resume-md-skill/tree/ea92c361ea61d86e2a028da2cf95ada4c55e33b3) | `baseline_pass_on_supported_platform` | WSL Ubuntu 原 CLI 输出中文一页，Noto Sans SC 字体下载成功；原生 Windows 不在上游支持范围。 |
| [chasen-resume-skills](https://github.com/Chasen-Liao/resume-skills/tree/3e5b8f61c81349ed9b4b5113c4faf8b4ac8f6992) | `conditional_visual_issue` | Edge 适配后原渲染器通过；Canvas 编辑、保存、读回及重导出已操作验证。短稿出现大段纵向留白，需调布局。默认 Chromium 下载在本次环境超时。 |
| [resume-optimizer](https://github.com/wyh0626/resume-optimizer/tree/fb16670c07bf22cce8c8a9b8494bbd693ea4651c) | `single_session_only` | 按上游流程做一次中文样例审计，保留团队归属与未测量项；非独立或重复模型评测，无排版器验收。 |
| [resume-coach](https://github.com/leemysw/skills/tree/c74119813aa295331e21d07e04cc86a377a16956) | `partial_parser_and_single_session` | 中文诊断单次演练完成；MD/PDF 解析保留检查项。DOCX 解析只读普通段落，漏掉表格中的公司、学校和项目标题，不可直接信任诊断。 |
| [repo-to-resume-tailor](https://github.com/Ssabby1/repo-to-resume-tailor/tree/6d2f526b15a6e8f6796e5953d48d7130a06def61) | `single_session_only` | 用虚构仓库做一次中文证据演练，区分本人函数与参考模板；不证明真实履历收益或重复执行质量。 |
| [resume-builder-cn](https://github.com/LittleDrunkWang/resume-builder-cn/tree/82f90483ca06984060848f4521ff7aabc872726a) | `template_only` | 入口 YAML 有效。上游可编辑模板填入同一虚构样例后用 Edge 导出通过；没有执行完整访谈、岗位研究及其原导出脚本。 |
| [init-resume-builder](https://github.com/INIT1996/resume-builder/tree/c710c4d7d00b8b245cf7913c9a989a3c1bebae0d) | `baseline_only_stress_fail` | 入口 YAML 有效。样例模板单页通过；多块长文示例分页生成 5 页，7 个压力编号的完整正文不可提取，页面边缘可见裁切。 |
| [resume-md2pdf](https://github.com/HduSy/resume-md2pdf/tree/44c511605b7efbaf9a51715fd15bb7c6c4993a03) | `conditional` | 上游建 HTML 和导出脚本使用 Edge，中文技术词混排样例及 40 条长文通过。上游仍明确不支持混排，不将一次成功扩展为通用支持。 |
| [resume-factory](https://github.com/hyf020908/resume-factory/tree/2fd9453f6fa90c39e70e30f6c8cb3e22c710f293) | `blocked_environment` | 真实上游模板的 XeLaTeX 编译探针缺 TikZ shadows.blur，未生成 PDF；不是完整中文样例通过。未为测试安装全局 TeX 包。 |

## 重要失败和复测

### RenderCV：中文六主题通过，长文需开启跨页

engineeringresumes、classic、harvard、engineeringclassic、sb2nov、moderncv 各生成一页 A4，中文正文、联系信息和教育标记完整。显式指定 Microsoft YaHei 和 `mandarin_chinese`。

40 条压力内容在默认不可跨页设置下生成 3 页，末条越出页面；即使 PDF 能提取这条文字，视觉仍然裁切。设置以下选项后重渲染为 2 页，40 条完整，边界及目视检查通过：

```yaml
design:
  entries:
    allow_page_break: true
  sections:
    allow_page_break: true
```

### cosen：字体是实际前提

Windows 原生 WeasyPrint 因缺 `libgobject-2.0-0` 阻塞。上游 `--html-only` 生成五套模板，再由测试适配器调用 Edge 打印为 PDF；这五套一页样例通过。compact 增加 40 条后为 2 页，完整保留。

WSL 首次 WeasyPrint 返回成功，但没有可用 CJK 字体，中文消失，判失败。向私有字体缓存注册 Noto Sans SC 并配置 fontconfig 后，compact 原渲染脚本复测通过。没有修改全局字体或声称其他四主题已走 WSL 原 PDF 路线。

### Word：输入语法和解析路径影响结果

JSON-Resume 使用自有 JSON 契约，标签联系人显式给 `href: null` 后生成 DOCX，Word 实际导出一页 PDF；中文与检查项完整。它不等同于 jsonresume.org 数据标准。

Denis 的 resume-layout-skill 对普通 Markdown 很敏感：求职意向放在联系信息前会提前结束头部解析，教育的三级标题也不符合其列表语法，初次输出漏邮箱、所在地和教育。改成其要求的格式后内容保留；但未给学校所在地时，脚本使用个人所在地填到学校，**仍属未经来源支持的新增信息**。因此不将其标成严格保真通过。

resume-coach 的 DOCX parser 只取 `document.paragraphs`，漏掉 JSON-Resume 表格中的公司、学校、学历和项目标题；退出码 0 不能作为完整读取的证明。同一份 PDF 与 Markdown 的检查标记保留。正式审稿前应核对解析结果，优先 PDF / Markdown。

### HTML：单页成功不能推导分页成功

INIT 示例模板填入基础样例后为 1 页；长文以 40 个独立 section 测其分页器，得到 5 页，但编号 9、10、19、20、29、30、39 的完整正文不能提取，页边可见裁切。此构造不同于 RenderCV / cosen / Hdu 的单个长列表，只用于暴露该示例的分页边界，不比较页数优劣。没有擅自修补上游后声称原版通过。

Chasen 的默认 Chromium 下载本次超时；通过适配器让原渲染脚本使用已安装 Edge 后成功。Canvas 实际完成中文姓名与字号编辑、保存、磁盘读回和重新导出。短简历模板存在大块纵向留白，自动检查通过仍需人工排版。LittleDrunk 只测试现有可编辑模板的填充和 Edge 导出，未走完整访谈与岗位研究。

Hdu 使用自定义中文字体 CSS、原 `build_html.mjs` 与 `render_pdf.mjs`，通过环境变量指定 Edge，基础一页及 40 条两页测试通过。但上游规则仍声明不做中英混排，本轮只能证明所给技术词样例有效。

### resume-factory：依赖阻塞，保留未知

对真实上游模板做 XeLaTeX 编译探针，缺 TikZ `shadows.blur` 库，未生成 PDF。它未完成统一样例测试；不据此断言上游无法支持中文，也不视为可直接推荐。原规则允许极小字号及要求照片的限制继续保留。

## 内容工作流测试的限制

三个内容类项目由当前 Agent 阅读各自规则后，在同一会话做一次引导式练习；没有独立模型调用日志、盲测评审、重复采样、对照组或面试结果。练习保留了团队归属、样本边界及未测量项，没有把 JD 中 Rust 补成已有技能；其中 coach 分数只是提示词量表的主观评分。**这些是可用性演练，不是三个项目准确率或排名的证据。**

repo-to-resume-tailor 使用本地虚构小仓库，个人范围只覆盖标签归一化函数，参考模板的整体调度不算个人独立研发；没有生产规模或收益可供推断。

## 环境与复现

- Windows 隔离 Python 环境：RenderCV 2.8、WeasyPrint 70.0（Windows 原生依赖失败）、Playwright；DOCX 到 PDF 使用本机 Microsoft Word COM。
- WSL Ubuntu：上游 ResumeMD CLI；cosen 在隔离环境约束 `weasyprint<67`，使用项目私有 Noto Sans SC 缓存及 fontconfig。
- Chasen 的 Playwright 与 Hdu 的 Puppeteer 都通过适配使用已安装 Microsoft Edge；这不是默认浏览器下载路线的通过。
- 固定源码 commit 见本页每行链接及 [results.json](results.json)。测试后上游默认分支变化不在本结果内。
- [fixtures](fixtures/) 提供统一输入与经记录的适配输入。没有上传真实简历、内部代码、完整上游源码、环境目录或含本机路径的原始操作日志。
- [check_pdf.py](check_pdf.py) 可检查任意生成 PDF 的基础文字与边界；安装 PyMuPDF 后执行 `python check_pdf.py resume.pdf`。它不能替代查看页面图像，也不能证明 ATS 解析成功。

RenderCV 复现示例（已安装相同版本及 Microsoft YaHei 时）：

```sh
rendercv render fixtures/rendercv.yaml -o output
rendercv render fixtures/rendercv-dense-breakable.yaml -o output-dense
```

其他项目请检出表内固定 commit，按各自上游文档安装依赖，再使用对应输入。`resume-fixed.json` 是 JSON-Resume 的适配输入，`docx-adapted.md` 是 Denis 的适配输入；Denis 的教育所在地默认行为仍需用户审查。测试中适配不是对上游源代码的修复提交。

完整结构化结果含初始失败和修复后的产物摘要及 SHA-256，见 [results.json](results.json)。失败不从记录中删除。本次不构成安全审计、全平台兼容保证、ATS 认证或真实求职效果验证。
