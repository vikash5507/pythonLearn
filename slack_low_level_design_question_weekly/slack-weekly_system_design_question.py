'''
Follow these steps to configure the webhook in Slack:

  1. Navigate to https://<your-team-domain>.slack.com/services/new

  2. Search for and select "Incoming WebHooks".

  3. Choose the default channel where messages will be sent and click "Add Incoming WebHooks Integration".

  4. Copy the webhook URL from the setup instructions and use it in the next section.

To encrypt your secrets use the following steps:

  1. Create or use an existing KMS Key - http://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html

  2. Expand "Encryption configuration" and click the "Enable helpers for encryption in transit" checkbox

  3. Paste <SLACK_CHANNEL> into the slackChannel environment variable

  Note: The Slack channel does not contain private info, so do NOT click encrypt

  4. Paste <SLACK_HOOK_URL> into the kmsEncryptedHookUrl environment variable and click "Encrypt"

  Note: You must exclude the protocol from the URL (e.g. "hooks.slack.com/services/abc123").

  5. Give your function's role permission for the `kms:Decrypt` action using the provided policy template
'''

import random
import boto3
import json
import logging
import os
import requests

from base64 import b64decode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


# The base-64 encoded, encrypted key (CiphertextBlob) stored in the kmsEncryptedHookUrl environment variable
ENCRYPTED_HOOK_URL = os.environ['kmsEncryptedHookUrl']
# The Slack channel to send a message to stored in the slackChannel environment variable
SLACK_CHANNEL = os.environ['slackChannel']

# HOOK_URL = "https://" + boto3.client('kms').decrypt(
#     CiphertextBlob=b64decode(ENCRYPTED_HOOK_URL),
#     EncryptionContext={'LambdaFunctionName': os.environ['AWS_LAMBDA_FUNCTION_NAME']}
# )['Plaintext'].decode('utf-8')

HOOK_URL = SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

logger = logging.getLogger()
logger.setLevel(logging.INFO)
low_level_solution_base_url = "https://s3.ap-south-1.amazonaws.com/3dev.com/"


def get_question():
    """
        Get random Problem statement from list 
    """

    low_level_system_design_question = {
        "1": {
            "problem_statement": "Stack Overflow is one of the largest online communities for developers to learn and share their knowledge. The website provides a platform for its users to ask and answer questions, and through membership and active participation, to vote questions and answers up or down. Users can edit questions and answers in a fashion similar to a wiki. Users of Stack Overflow can earn reputation points and badges. For example, a person is awarded ten reputation points for receiving an UPVote on an answer and five points for the UPVote of a question. The can also receive badges for their valued contributions. A higher reputation lets users unlock new privileges like the ability to vote, comment on, and even edit other peoples posts.",
            "pages": [
                "StackOverflow.html",
                "StackOverflow2.html",
                "StackOverflow3.html"
            ]
        },
        "2": {
            "problem_statement": "Amazon is the worlds largest online retailer. The company was originally a bookseller but has expanded to sell a wide variety of consumer goods and digital media. For the sake of this problem, we will focus on their online retail business where users can sell and buy their products.",
            "pages": ["Amazon.html", "Amazon2.html", "Amazon3.html"]
        },
        "3": {
            "problem_statement": "A parking lot or car park is a dedicated cleared area that is intended for parking vehicles. In most countries where cars are a major mode of transportation, parking lots are a feature of every city and suburban area. Shopping malls, sports stadiums, megachurches, and similar venues often feature parking lots over large areas.",
            "pages": ["ParkingLot.html", "ParkingLot2.html", "ParkingLot3.html"]
        },
        "4": {
            "problem_statement": "An Online Stock Brokerage System facilitates its users the trade i.e. buying and selling of stocks online. It allows clients to keep track of and execute their transactions, and shows performance charts of the different stocks in their portfolios. It also provides security for their transactions and alerts them to pre-defined levels of changes in stocks, without the use of any middlemen. The online stock brokerage system automates traditional stock trading using computers and the internet, making the transaction faster and cheaper. This system also gives speedier access to stock reports, current market trends, and real-time stock prices.",
            "pages": [
                "OnlineStockBrokerageSystem.html",
                "OnlineStockBrokerageSystem2.html"
            ]
        },
        "5": {
            "problem_statement": "An Airline Management System is a managerial software which targets to control all operations of an airline. Airlines provide transport services for their passengers. They carry or hire aircraft for this purpose. All operations of an airline company are controlled by their airline management system. This system involves the scheduling of flights, air ticket reservations, flight cancellations, customer support, and staff management. Daily flights updates can also be retrieved by using the system.",
            "pages": [
                "AirlineManagementSystem.html",
                "AirlineManagementSystem2.html",
                "AirlineManagementSystem3.html"
            ]
        },
        "6": {
            "problem_statement": "A Library Management System is a software built to handle the primary housekeeping functions of a library. Libraries rely on library management systems to manage asset collections as well as relationships with their members. Library management systems help libraries keep track of the books and their checkouts, as well as members subscriptions and profiles. Library management systems also involve maintaining the database for entering new books and recording books that have been borrowed with their respective due dates.",
            "pages": ["LibraryManagementSystem.html", "LibraryManagementSystem2.html"]
        },
        "7": {
            "problem_statement": "An online movie ticket booking system facilitates the purchasing of movie tickets to its customers. E-ticketing systems allow customers to browse through movies currently playing and book seats, anywhere and anytime.",
            "pages": [
                "MovieTicketBookingSystem.html",
                "MovieTicketBookingSystem2.html",
                "MovieTicketBookingSystem3.html"
            ]
        },
        "8": {
            "problem_statement": "Blackjack is the most widely played casino game in the world. It falls under the category of comparing-card games and is usually played between several players and a dealer. Each player, in turn, competes against the dealer, but players do not play against each other. In Blackjack, all players and the dealer try to build a hand that totals 21 points without going over. The hand closest to 21 wins.",
            "pages": [
                "Blackjack_a_Deck_of_Cards.html",
                "Blackjack_a_Deck_of_Cards2.html"
            ]
        },
        "9": {
            "problem_statement": "An automated teller machine ATM is an electronic telecommunications instrument that provides the clients of a financial institution with access to financial transactions in a public space without the need for a cashier or bank teller. ATMs are necessary as not all the bank branches are open all days of the week, and some customers may not be in a position to visit a bank each time they want to withdraw or deposit money.",
            "pages": ["ATM.html", "ATM2.html"]
        },
        "10": {
            "problem_statement": "A Hotel Management System is a software built to handle all online hotel activities easily and safely. This System will give the hotel management power and flexibility to manage the entire system from a single online portal. The system allows the manager to keep track of all the available rooms in the system as well as to book rooms and generate bills.",
            "pages": [
                "HotelManagementSystem.html",
                "HotelManagementSystem2.html",
                "HotelManagementSystem3.html"
            ]
        },
        "11": {
            "problem_statement": "A Restaurant Management System is a software built to handle all restaurant activities in an easy and safe manner. This System will give the Restaurant management power and flexibility to manage the entire system from a single portal. The system allows the manager to keep track of available tables in the system as well as the reservation of tables and bill generation.",
            "pages": [
                "RestaurantManagementSystem.html",
                "RestaurantManagementSystem2.html",
                "RestaurantManagementSystem3.html"
            ]
        },
        "12": {
            "problem_statement": "Chess is a two player strategy board game played on a chessboard, which is a checkered gameboard with 64 squares arranged in an `8??8` grid. There are a few versions of game types that people play all over the world. In this design problem, we are going to focus on designing a two-player online chess game.",
            "pages": ["Chess.html", "Chess2.html"]
        },
        "13": {
            "problem_statement": "A Car Rental System is a software built to handle the renting of automobiles for a short period of time, generally ranging from a few hours to a few weeks. A car rental system often has numerous local branches `to allow its user to return a vehicle to a different location`, and primarily located near airports or busy city areas.",
            "pages": [
                "CarRentalSystem.html",
                "CarRentalSystem2.html",
                "CarRentalSystem3.html"
            ]
        },
        "14": {
            "problem_statement": "LinkedIn is a social network for professionals. The main goal of the site is to enable its members to connect with people they know and trust professionally, as well as to find new opportunities to grow their careers. A LinkedIn member's profile page, which emphasizes their skills, employment history, and education, has professional network news feeds with customizable modules. LinkedIn is very similar to Facebook in terms of its layout and design. These features are more specialized because they cater to professionals, but in general, if you know how to use Facebook or any other similar social network, LinkedIn is somewhat comparable.",
            "pages": ["LinkedIn.html", "LinkedIn2.html"]
        },
        "15": {
            "problem_statement": "Cricinfo is a sports news website exclusively for the game of cricket. The site features live coverage of cricket matches containing ball-by-ball commentary and a database for all the historic matches. The site also provides news and articles about cricket.",
            "pages": ["Cricinfo.html", "Cricinfo2.html"]
        },
        "16": {
            "problem_statement": "Facebook is an online social networking service where users can connect with other users to post and read messages. Users access Facebook through their website interface or mobile apps.",
            "pages": ["Facebook.html", "Facebook2.html"]
        }
    }

    problem_num = os.environ['nextProblemNumber']
    total_problems = os.environ['totalProblems']

    problem = low_level_system_design_question.get(
        str(problem_num), random.randint(1, 16))

    problem_of_the_week = {
        "problem": problem.get("problem_statement"),
        "solution": problem.get("pages")
    }

    if int(problem_num) == int(total_problems):
        problem_num = "0"

    os.environ['nextProblemNumber'] = str(int(problem_num) + 1)

    return problem_of_the_week


def lambda_handler(event, context):
    #logger.info("Event: " + str(event))

    message = get_question()

    formatted_message = "*Question Low Level Design:*\n\n>" + \
        message.get("problem")+"\n\n *Solution*\n\n>"

    for sol_url in message.get("solution"):
        full_url = low_level_solution_base_url + sol_url
        formatted_message += "\n\n><"+full_url+"|"+sol_url+">"

    # formatted_message += "\n"
    print(os.environ['nextProblemNumber'])
    slack_message = {
        'channel': SLACK_CHANNEL,
        # 'text': json.dumps(message.get("problem"))
        'text': formatted_message
    }

    # headers = {'Content-Type': 'application/json'}
    req = Request(HOOK_URL, json.dumps(slack_message).encode('utf-8'))
    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
