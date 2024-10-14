# git notes

#### Get current commit hash
```bash
git rev-parse HEAD
```

#### Get root directory of repo
```bash
git rev-parse --show-toplevel
```

#### List files changed in a commit
```bash
git diff-tree --no-commit-id --name-only -r <commit>
```

#### Get commit date of single file
```bash
git log -1 --format=%ci <filename>
```

#### Get commit date of all files in a repo
```bash
git ls-tree -r --name-only HEAD -z | TZ=UTC xargs -0n1 -I_ git --no-pager log -1 --date=iso-local --format="%ad _" -- _
```
#### List all files in repo and their corresponding commit hash
```bash
git ls-files -z | GIT_PAGER= xargs -0 -L1 -I'{}' git log -n 1 --format=\"%h {}\" -- '{}'
```
