from setuptools import setup, find_packages

setup(
    name="daily-summary",
    version="0.1.22",
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
        "openai",
        "gitpython",
        "python-dotenv",
        "pytest",
    ],
    python_requires=">=3.11",
    # Additional metadata about your package
    author="Jack Driscoll",
    author_email="jackdriscoll777@gmail.com",
    description="A package to generate daily development reports",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jdriscoll98/daily-summary",
    entry_points={
        "console_scripts": [
            "daily-summary=daily_summary.main:main",
            "publish=daily_summary.publish:main",
            "test=pytest:main",
        ],
    },
)
