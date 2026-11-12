name: semgrep
on:
  pull_request:
    branches: [main]


jobs:
  semgrep:
    runs-on: ubuntu-latest
    container:
      image: semgrep/semgrep
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - run: |
          git config --global --add safe.directory "$GITHUB_WORKSPACE"
          semgrep scan --config p/python --config p/owasp-top-ten\
            --baseline-commit "${{ github.event.pull_request.base.sha }}" --error
