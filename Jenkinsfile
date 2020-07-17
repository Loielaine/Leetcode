#!groovy

//Documentation: https://confluence.expedia.biz/display/ECT/Egencia+Jenkins+Blue+Ocean
serviceName = JOB_NAME.replaceAll(/-pipeline.*/, "")
serviceOwner = "nrahal"
branch = env.BRANCH_NAME

MASTER_BRANCH = "master"

try {
    switch (branch) {
        case MASTER_BRANCH:
            masterPipeline()
            break
        default:
            //runs pr builds
            branchPipeline()
    }
    postCompletionSuccess()
} catch (Exception error) {
    //marks the build as failure when there is an exception
    postCompletionFailed(error: error)
}


def masterPipeline() {
    egenciaPythonBuild(slackChannel: '#ege-fake-slack-room')
}


def branchPipeline() {
    egenciaPythonPullRequestBuild(slackChannel: '#ege-fake-slack-room')
}