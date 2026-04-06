# GitHub 同步方案

## 原则

- 用 GitHub 做版本管理和跨设备同步
- 不把敏感配置和大附件直接公开同步
- Obsidian 负责记，Git 负责保存历史

## 推荐仓库形态

- 最好用私有仓库
- 一个 vault 一个仓库
- 附件很多时，再单独考虑云盘，不要先把 Git 用坏

## 这个 vault 已经做的保护

- `.gitignore` 已排除 `workspace.json`
- `.gitignore` 已排除 `Local REST API` 的敏感配置
- `.gitignore` 已排除 `07 Resources` 下的大附件

## 本地初始化

```bash
cd "/Users/bai/Documents/Obsidian/Space"
git init
git add .
git commit -m "Initialize Obsidian workspace"
```

## 接 GitHub 私有仓库

```bash
cd "/Users/bai/Documents/Obsidian/Space"
git remote add origin <your-private-repo-url>
git branch -M main
git push -u origin main
```

## 在 Obsidian 里怎么用 Git 插件

- 打开 Command Palette
- 搜 `Obsidian Git: Create backup`
- 搜 `Obsidian Git: Pull`
- 搜 `Obsidian Git: Open source control view`

## 建议节奏

- 每天收工前 `Create backup`
- 换设备前先 `Create backup`
- 开始工作前先 `Pull`

## 不建议

- 不要把公开仓库当默认选项
- 不要把证书、token、客户隐私信息直接推上去
- 不要让插件自动每几分钟 commit，一般会把历史刷烂

