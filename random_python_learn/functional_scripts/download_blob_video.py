import requests

# SONY_LIVE_BLOB_URL = "blob:https://www.sonyliv.com/206f4bcc-b5f9-4127-8925-a461f2076e80"

# a = "https://securetoken.sonyliv.com/DASH/3bd23585-9fbc-429b-896b-ba88c2b80a38/show_set_STI_ep23_india_20220119T134618_5500k_20220119T142802_000000049.mp4?hdntl=exp=1643651400~acl=/*~hmac=2997c1e4d77559f12556047b07fb1000592464f663e08c9552945f89ad12feac"


headers = {
    'authority': 'securetoken.sonyliv.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'x-playback-session-id': '4bea7024d1d14e159769c53142bc9c65-1641575808362',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'accept': '*/*',
    'origin': 'https://www.sonyliv.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8',
}

params = (
    ('hdntl', 'exp=1643651400~acl=/*~hmac=2997c1e4d77559f12556047b07fb1000592464f663e08c9552945f89ad12feac'),
)

response = requests.get(
    'https://securetoken.sonyliv.com/DASH/3bd23585-9fbc-429b-896b-ba88c2b80a38/show_set_STI_ep23_india_20220119T134618_Hindi64k_20220119T142802_000000049.mp4',
    headers=headers,
    params=params,
    stream=True)

CHUNK_SIZE = 256

with open("sonyliv.mp4", "wb") as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        f.write(chunk)


# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://securetoken.sonyliv.com/DASH/3bd23585-9fbc-429b-896b-ba88c2b80a38/show_set_STI_ep23_india_20220119T134618_Hindi64k_20220119T142802_000000049.mp4?hdntl=exp=1643651400~acl=/*~hmac=2997c1e4d77559f12556047b07fb1000592464f663e08c9552945f89ad12feac', headers=headers)
