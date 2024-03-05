This is an advanced example for managing CI/CD across multiple Prefect workspaces.

The GitHub Actions workflows in this repo 
- create mirrored deployments across staging and prod workspaces.
    - Which workspace flows are deployed to is determined by the branch that changes happen on: `stg` for staging, `main` for prod.
- build and push docker images that do _not_ contain flow code, and are tagged like `:<commit-hash>-<environment>` to tie the code version and branch/env to image versions
- cache both docker image layers and pip dependencies for ultra fast rebuilds, rather than try to be creative with different routes through the deployment process
- push code to S3 (via the `push` step of each `prefect.yaml`), where:
    - each environment gets its own bucket
    - each project gets its own folder in that bucket

This example demonstrates a monorepo approach with multiple projects, each project having:
- a `prefect.yaml`
- a `Dockerfile`
- a `requirements.txt`
- its own flow(s)
- its own independently triggered GitHub Actions workflow

The configuration files heavily rely on templating to make copy/pasting files when starting new projects or adding deployments easier.
