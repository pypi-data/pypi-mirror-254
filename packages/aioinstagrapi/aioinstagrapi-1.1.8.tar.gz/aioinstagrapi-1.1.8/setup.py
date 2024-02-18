from setuptools import find_packages, setup

long_description = """
Fast and effective asynchronous Instagram Private API wrapper (public+private requests and challenge resolver).

Uses the most recent version of the API from Instagram.

Async wrapper around https://githib.com/adw0rd/instagrapi

Features:

1. Performs Public API (web, anonymous) or Private API (mobile app, authorized)
   requests depending on the situation (to avoid Instagram limits)
2. Challenge Resolver have Email (as well as recipes for automating receive a code from email) and SMS handlers
3. Support upload a Photo, Video, IGTV, Clips (Reels), Albums and Stories
4. Support work with User, Media, Insights, Collections, Location (Place), Hashtag and Direct objects
5. Like, Follow, Edit account (Bio) and much more else
6. Insights by account, posts and stories
7. Build stories with custom background, font animation, swipe up link and mention users
8. In the next release, account registration and captcha passing will appear
"""

requirements = ['aioconsole==0.6.2', 'aiofiles==23.2.1', 'anyio==4.0.0', 'awaits==0.0.4', 'black==23.11.0', 'certifi==2023.7.22', 'charset-normalizer==3.3.2', 'click==8.1.7', 'curlify2==2.0.0', 'decorator==4.4.2', 'exceptiongroup==1.1.3', 'h11==0.14.0', 'httpcore==1.0.2', 'httpx==0.25.1', 'idna==3.4', 'imageio==2.32.0', 'imageio-ffmpeg==0.4.9', 'moviepy==1.0.3',
                'mypy-extensions==1.0.0', 'numpy==1.24.4', 'packaging==23.2', 'pathspec==0.11.2', 'Pillow==10.0.1', 'platformdirs==4.0.0', 'proglog==0.1.10', 'pycryptodomex==3.18.0', 'pydantic==1.10.9', 'PySocks==1.7.1', 'requests==2.31.0', 'requests-to-curl==1.1.0', 'sniffio==1.3.0', 'tenacity==8.2.3', 'tomli==2.0.1', 'tqdm==4.66.1', 'typing-extensions==4.8.0', 'urllib3==2.1.0']

setup(
    name="aioinstagrapi",
    version="1.1.8",
    author="Joshua Solo",
    author_email="policeoser@gmail.com",
    license="MIT",
    url="https://github.com/ragedotdev/aioinstagrapi",
    install_requires=requirements,
    keywords=[
        "instagram private api",
        "instagram-private-api",
        "instagram api",
        "instagram-api",
        "instagram",
        "instagram-scraper",
        "instagram-client",
        "instagram-stories",
        "instagram-feed",
        "instagram-reels",
        "instagram-insights",
        "downloader",
        "uploader",
        "videos",
        "photos",
        "albums",
        "igtv",
        "reels",
        "stories",
        "pictures",
        "instagram-user-photos",
        "instagram-photos",
        "instagram-metadata",
        "instagram-downloader",
        "instagram-uploader",
        "instagram-note",
    ],
    description="Fast and effective asynchronous Instagram Private API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
