# Patched!

`patched-cli` is a CLI that generates vulnerability patches for your codebase.

## Quickstart guide

1. Install patched-cli.
   ```shell
   pip install patched-cli
   ```
2. Run `patched-cli` with your git repository as its argument or working directory.
   When the working directory is the git repository
   ```shell
   patched-cli
   ```
   When the argument is the git repository
   ```shell
   patched-cli /path/to/my/git/repository
   ```
3. If this is the first time running `patched-cli`, you will be redirected to patched's
[sign-in page](https://patched.codes/signin) to generate a token. Copy the token and paste it to the prompt.
If this is not the first time running `patched-cli` an application directory should already exist under your user's
home directory if you are using a Unix-based operating system or 
AppData folder if you are using a windows based operating system.
Alternatively you can set the environment variable `PATCHED_ACCESS_TOKEN` before running `patched-cli`.
   ```shell
   export PATCHED_ACCESS_TOKEN="your-patched-access-token-here"
   patched-cli 
   ```
4. To create a pull request you can set the `--create-pr` flag. 
   ```shell
   patched-cli --create-pr
   ```
   If `patched.codes` is not installed in your GitHub repository you can give `patched-cli` your 
   GitHub Personal Access Token via the option `--github-access-token` or set the environment variable `PATCHED_GITHUB_TOKEN`
   ```shell
   export PATCHED_GITHUB_TOKEN="your.patched.access.token.here"
   patched-cli --create-pr
   ```

## Extras for Windows users
`patched-cli` only supports Windows using WSL(Windows Subsystem for Linux). Please consult [WSL install](https://learn.microsoft.com/en-us/windows/wsl/install) for more information.