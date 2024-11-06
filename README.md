This is an advanced example for managing CI/CD across multiple Prefect workspaces.

The GitHub Actions workflows in this repo: 
- create mirrored deployments across staging and prod workspaces
    - which workspace flows are deployed to is determined by the branch that changes happen on:
        - a pull request on any branch updates deployments in the staging workspace
        - a merge to `main` updates deployments in the prod workspace
- build and push docker images that do _not_ contain flow code, and are tagged like `:<commit-hash>-<environment>` to tie the code version and branch/env to image versions
- cache both docker image layers and pip dependencies for ultra fast rebuilds
- push code to S3 (via the `push` step of each `prefect.yaml`), where:
    - each environment gets its own bucket
    - each project gets its own folder in that bucket

This example demonstrates a monorepo approach with multiple projects, each project having:
- a `prefect.yaml`
- a `Dockerfile`
- a `requirements.txt`
- its own flow(s)
- its own independently triggered GitHub Actions workflow

The configuration relies heavily on templating to make copy/pasting files when starting new projects or adding deployments easier.
