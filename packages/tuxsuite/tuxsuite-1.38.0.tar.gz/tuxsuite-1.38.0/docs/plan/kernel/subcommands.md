# Sub-commands

## cancel

`cancel` is a subcommand for cancelling submitted plan identified by its `uid`.
Cancelling is available for any build/oebuild/test state, except `finished`.

```
tuxsuite plan cancel 1t2giSA1sSKFADKPrl0YI1gjMLb
```

## get

`get` is a subcommand which fetches the details for the plan
identified by its `uid`.

```
tuxsuite plan get 1t2gzLqkWHi2ldxDETNMVHPYBYo
```

## list

`list` is a subcommand which fetches the latest 30 plans by default.

```
tuxsuite plan list
```

In order to restrict the number of plans fetched, `--limit` is used
as follows:

```
tuxsuite plan list --limit 5
```

To get the output of the above commands in JSON format, use the
following:

```
tuxsuite plan list --json --limit 2
```

## submit

`submit` is a subcommand for submitting plan files.

```
tuxsuite plan submit plan.yaml
```

## wait

`wait` is a subcommand which fetches the details for the plan identified
by its `uid`, if the plan is in progress, it will update the details
on screen. This will be handy to submit a plan and come back at a
later point of time to watch the plan's progression.

```
tuxsuite plan wait 1yiHhE3rnithNxBudqxCrWBlWKp
```

## create

`create` is a subcommand to generate a plan file from individual build/test plan file.
This subcommand takes `--build-plan` and `--test-plan` Path/URL as input to produce a plan which
consists of build from build plan file and test from test plan file. The options `--build-plan`
and `--test-plan` can be utilized either individually or in combination with other [options](#options)
to generate a plan.

!!! note "Note"
    This subcommand takes a build/test plan file that contains only a single build or test job

!!! info "example"

    * Generate a plan with both build and test

    ```shell
    tuxsuite plan create --build-plan <build-plan.yaml/URL> --test-plan <test-plan.yaml/URL>
    ```

    * Generate a plan from build plan

    ```shell
    tuxsuite plan create --build-plan <build-plan.yaml/URL>
    ```

    * Generate a plan from test plan

    ```shell
    tuxsuite plan create --test-plan <test-plan.yaml/URL>
    ```

### Options

The `create` subcommand supports the following options:

* `--build-plan`: Path/URL to build plan file.
* `--test-plan`: Path/URL to test plan file.
* `--test-retrigger`: Number of times test has to be retriggered. Defaults to 1.
* `--overwrite-target`: Targets to be overwritten to build job. Specific to build plan only.
* `--append-kconfig`: Kconfig to append to build job. Specific to build plan only.
* `--output-plan`: Output plan file path.
