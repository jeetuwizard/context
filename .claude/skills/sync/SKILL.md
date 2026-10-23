---
name: sync
description: Keep the context repo current — record progress, decisions, or new info in the right doc, then commit and push to GitHub. Use whenever something gets done or decided (a checklist item finishes, a new account or link, a teammate's name, an upload speed, a new asset), or when the user says sync, save, update context, or push.
---

# Sync the context repo

The repo is the memory of this project across Claude sessions. If it isn't written here, the next session won't know it.

## Where each kind of update goes

| What changed | File |
|---|---|
| Checklist item done, new pending item | `docs/06-checklists.md` |
| Account, handle, link, teammate channel | `docs/01-brand-and-accounts.md` (and `README.md` quick links if it's a main link) |
| Hardware, OBS settings, upload speed | `docs/02-streaming-setup.md` |
| Teammate names, roles, permissions, workflow | `docs/03-team-and-workflow.md` |
| Bio or description text changed on a platform | `docs/04-texts.md` |
| Drive layout, local Drive mirror path | `docs/08-storage.md` |
| A new final decision | `CLAUDE.md` → "Decisions that are final" |
| Asset approved | PNG in `assets/final/`, source in `design-src/`, job in `scripts/render-assets.ps1` |

Update the "Status as of" date in `docs/06-checklists.md` when ticking items.

## Commit and push

```bash
git status
git add -A
git commit -m "<what changed, in plain words>"
git push
```

Before committing, check `git status` for anything that shouldn't be there: videos, personal phone numbers, passwords, 2FA backup codes. Those never go in the repo, even though it's private.

End the commit message with the attribution trailer configured for this session, if any.
