import requests
import json


LEETCODE_URL = "https://leetcode.com"

LEETCODE_PROBLEMSET_URL = "https://leetcode.com/problemset/all/"

LEETCODE_GRAPHQL_API = "https://leetcode.com/graphql"

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"


def send_message_to_slack():
    pass


def get_question_using_api():
    """
        Get Problem statement directly using graphQL library
    """
    graphql_query_data = {"query": "query questionOfToday {\n\tactiveDailyCodingChallengeQuestion {\n\t\tdate\n\t\tuserStatus\n\t\tlink\n\t\tquestion {\n\t\t\tacRate\n\t\t\tdifficulty\n\t\t\tfreqBar\n\t\t\tfrontendQuestionId: questionFrontendId\n\t\t\tisFavor\n\t\t\tpaidOnly: isPaidOnly\n\t\t\tstatus\n\t\t\ttitle\n\t\t\ttitleSlug\n\t\t\thasVideoSolution\n\t\t\thasSolution\n\t\t\ttopicTags {\n\t\t\t\tname\n\t\t\t\tid\n\t\t\t\tslug\n\t\t\t}\n\t\t}\n\t}\n}\n", "operationName": "questionOfToday"}
    header = {"Content-Type": "application/json"}

    question_data = requests.post(
        LEETCODE_GRAPHQL_API, data=json.dumps(graphql_query_data), headers=header)

    question_data = json.loads(question_data.text)
    print(question_data)
    question_of_the_day = question_data.get("data").get(
        "activeDailyCodingChallengeQuestion")

    response_context = {
        "problem_link": LEETCODE_URL + question_of_the_day.get("link"),
        "date": question_of_the_day.get("date"),
        "problem_title": question_of_the_day.get("question").get("title"),
        "dificulty": question_of_the_day.get("question").get("difficulty"),
        "acceptance_rate": question_of_the_day.get("question").get("acRate")
    }

    print(response_context)
    # return response_context


if __name__ == '__main__':
    get_question_using_api()
