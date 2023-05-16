# STOP PRESS
We're re-architecting. [HERE](https://github.com/Significant-Gravitas/Auto-GPT/wiki/Architecting)

^ READ THIS FIRST!

NOTE: We're in the process of moving content from the repo's CONTRIBUTING.md to here! To request a change to this doc, ask a maintainer on discord (@Maintainer will do it).

# 🎁 Contributing

😣 Larry is filing an issue. Larry is too lazy to read the [/docs](https://github.com/Significant-Gravitas/Auto-GPT/tree/master/docs). Larry is also too lazy to check for duplicates. Larry is even too lazy to talk in the Discord. Larry isn't supplying useful information in his issue. He hasn't even filled out the PR description. It's all rather a mess. Larry's issue will be closed.

😖 Curly is making a Pull Request. He's making a minor code-change and adding some punctuation in the doc. If he's honest with himself he wants to boost his GitHub stats to show he's contributed to AutoGPT. He's not taking on a difficult task, and his code is not bringing significant value. A Triager has to preprocess his PR, then a maintainer has to put it on the [Project Kanban](https://github.com/orgs/Significant-Gravitas/projects/1). Then it has to be reviewed by two maintainers before being merged. A core-dev could do this work in half the time it takes to process, so Curly is actually CREATING work for the coredev team. Curly's PR will be rejected.

😫 Moe is also making a Pull Request. This one's big. Moe is proud of it. But he hasn't bothered to look at the roadmap or even discuss with a maintainer/catalyst on the Discord what he's planning. He didn't create a draft PR with a statement of purpose. He just dived in. Alas the core team are going in a different direction. Moe's PR won't be making it in.

Don't be a stooge.

🦎 Bill the Lizard, on the other hand, has got it right:
- He's quietly figured out how the code works
- He's spotted a problem. It's quite a lot of work even for Bill, who is a senior software engineer. So that's likely to take a load off of the shoulders of the core-team.
- A quick search of issues / PRs suggests nobody's on it
- He's created a Draft-PR on GitHub and filled in the description
    - He's filled in the description
        - Clean summary of the problem he's addressing
        - Clean summary of how he's gona solve it
        - links to related resources
        - and he's put his DiscordId in too
- He's jumped on the Discord, and floated his proposal in the right channel (#dev-chat)
    - A maintainer has picked up and greenlighted his PR
    - Eddie the Eagle (also a quality contributor) had the same idea, but (while searching) sees Bill's draftPR and joins forces
- Bill writes code:
    - He uses ChatGPT/GPT4 sometimes to make sure he's using best practices
    - Eddie helps out by making PRs against Bill's PR, which Bill reviews and merges in
    - Bill and Eddie run the tests on the PR, so that they know it's gona pass the CI
    - They are careful to only focus on modifying relevant code
        They see plenty of unrelated code that can be tidied up, but they're keeping this PR focused
    - Wonderful, it's working!
- Bill removes the DRAFT status of his PR, hops on the Discord and sends a message in #pull-requests to say "Chekkit y'all!"
    - Actually he notices Pwuts is livestreaming, so hops in and they do a live review/merge.
- Bill's fix is now in master.
    - There is jubilance and great celebration throughout the realm.
    - Bill is offered a Contributors badge, as he fkn nailed it.

- Later Eddie eats Bill, because he is hungry and an Eagle is higher in the foodchain than a Lizard.

This is sad for us as Bill is exactly the kind of energy we need. We're looking for contributors like Bill.

🦅

DISCLAIMER: No lizards were harmed in the development of AutoGPT. The tale is apocryphal. We do have a coredev named Bill, but he is not (as far as we can tell) a lizard.

🎖️ This is how to get the **CONTRIBUTOR** badge in Discord -- our mergers are on the lookout for contributions that demonstrate a high level of engineering capability. If you put your Discord name in your PR we'll be able to contact you. 

- - -

```
Succinct notes for contributors
    How to contribute (github, discord)
        First check it's wanted/useful
            Roadmap (here)
            Discord
            File an issue / discussion / get approval
            Create empty draft PR and get it on the kanban
            Work on it, Discord is there
            Take it OFF draft to say "ready for review"
            Mention it in #pull-requests on Discord, can discuss, can help fast-track
            ALSO pwuts is livestreaming each day, he may merge it live for you
```

- - - 

NOTE: Below is the (as of 4 May 2023) CONTRIBUTING.md document. CONTRIBUTING.md's contents are being replaced with a hyperlink to **this page**. This is because this page acts as a single source of truth and a livedoc. 

- - -

# Contributing to Auto-GPT

First of all, thank you for considering contributing to our project! We appreciate your time and effort, and we value any contribution, whether it's reporting a bug, suggesting a new feature, or submitting a pull request.

This document provides guidelines and best practices to help you contribute effectively.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct]. Please read it to understand the expectations we have for everyone who contributes to this project.

[Code of Conduct]: https://docs.agpt.co/code-of-conduct/

## 📢 A Quick Word
Right now we will not be accepting any Contributions that add non-essential commands to Auto-GPT.

However, you absolutely can still add these commands to Auto-GPT in the form of plugins.
Please check out this [template](https://github.com/Significant-Gravitas/Auto-GPT-Plugin-Template).

## Getting Started

1. Fork the repository and clone your fork.
2. Create a new branch for your changes (use a descriptive name, such as `fix-bug-123` or `add-new-feature`).
3. Make your changes in the new branch.
4. Test your changes thoroughly.
5. Commit and push your changes to your fork.
6. Create a pull request following the guidelines in the [Submitting Pull Requests](#submitting-pull-requests) section.

## How to Contribute

### Reporting Bugs

If you find a bug in the project, please create an issue on GitHub with the following information:

- A clear, descriptive title for the issue.
- A description of the problem, including steps to reproduce the issue.
- Any relevant logs, screenshots, or other supporting information.

### Suggesting Enhancements

If you have an idea for a new feature or improvement, please create an issue on GitHub with the following information:

- A clear, descriptive title for the issue.
- A detailed description of the proposed enhancement, including any benefits and potential drawbacks.
- Any relevant examples, mockups, or supporting information.

### Submitting Pull Requests

When submitting a pull request, please ensure that your changes meet the following criteria:

- Your pull request should be atomic and focus on a single change.
- Your pull request should include tests for your change. We automatically enforce this with [CodeCov](https://docs.codecov.com/docs/commit-status)
- You should have thoroughly tested your changes with multiple different prompts.
- You should have considered potential risks and mitigations for your changes.
- You should have documented your changes clearly and comprehensively.
- You should not include any unrelated or "extra" small tweaks or changes.

## Style Guidelines

### Code Formatting

We use the `black` and `isort` code formatters to maintain a consistent coding style across the project. Please ensure that your code is formatted properly before submitting a pull request.

To format your code, run the following commands in the project's root directory:

```bash
python -m black .
python -m isort .
```

Or if you have these tools installed globally:
```bash
black .
isort .
```

### Pre-Commit Hooks

We use pre-commit hooks to ensure that code formatting and other checks are performed automatically before each commit. To set up pre-commit hooks for this project, follow these steps:

Install the pre-commit package using pip:
```bash
pip install pre-commit
```

Run the following command in the project's root directory to install the pre-commit hooks:
```bash
pre-commit install
```

Now, the pre-commit hooks will run automatically before each commit, checking your code formatting and other requirements.

If you encounter any issues or have questions, feel free to reach out to the maintainers or open a new issue on GitHub. We're here to help and appreciate your efforts to contribute to the project.

Happy coding, and once again, thank you for your contributions!

Maintainers will look at PR that have no merge conflicts when deciding what to add to the project. Make sure your PR shows up here:
https://github.com/Significant-Gravitas/Auto-GPT/pulls?q=is%3Apr+is%3Aopen+-label%3Aconflicts

## Testing your changes

If you add or change code, make sure the updated code is covered by tests.
To increase coverage if necessary, [write tests using pytest].

For more info on running tests, please refer to ["Running tests"](https://docs.agpt.co/testing/).

[write tests using pytest]: https://realpython.com/pytest-python-testing/

### API-dependent tests

To run tests that involve making calls to the OpenAI API, we use VCRpy. It caches known
requests and matching responses in so-called *cassettes*, allowing us to run the tests
in CI without needing actual API access.

When changes cause a test prompt to be generated differently, it will likely miss the
cache and make a request to the API, updating the cassette with the new request+response.
*Be sure to include the updated cassette in your PR!*

When you run Pytest locally:

- If no prompt change: you will not consume API tokens because there are no new OpenAI calls required.
- If the prompt changes in a way that the cassettes are not reusable:
    - If no API key, the test fails. It requires a new cassette. So, add an API key to .env.
    - If the API key is present, the tests will make a real call to OpenAI.
        - If the test ends up being successful, your prompt changes didn't introduce regressions. This is good. Commit your cassettes to your PR.
        - If the test is unsuccessful:
            - Either: Your change made Auto-GPT less capable, in that case, you have to change your code.
            - Or: The test might be poorly written. In that case, you can make suggestions to change the test.

In our CI pipeline, Pytest will use the cassettes and not call paid API providers, so we need your help to record the replays that you break.


### Community Challenges
Challenges are goals we need Auto-GPT to achieve.
For more information: https://docs-git-fork-merwanehamadi-featury-put-challen-20d77a-auto-gpt.vercel.app/challenges/introduction/