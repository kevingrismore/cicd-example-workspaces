This is an advanced example for managing CI/CD across multiple workspaces.

The GitHub Actions Workflows in this repo:

- create mirrored deployments across staging and prod workspaces
    - which workspace the flow gets deployed to is determined by the branch that changes happen on: stg for staging, main for prod
- demonstrates a monorepo approach with multiple projects, each project having:
    - a prefect.yaml
    - a Dockerfile
    - a requirements.txt
    - its own flow(s)
    - its own independently triggered github actions workflow
- builds and pushes docker images that do not contain flow code, and are tagged like :<commit-hash>-<environment> to tie the code version and branch/env to image versions
- caches both docker image layers and pip dependencies for ultra fast rebuilds, rather than try to be creative with different routes through the deployment process
- pushes and pulls code to and from S3, where:
    - each environment gets its own bucket
    - each project gets its own folder in that bucket
- heavily relies templating to make it easy to copy/paste files when starting new projects or adding deployments
