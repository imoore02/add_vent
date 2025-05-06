## AddVent Application ##

Description: A chrome extention that will scan any page and extract events, allowing a user to automatically add them to their
            google calendar.

Phases:
    1. Implement a NLP AI to scan text and produce structured output about the dates present.
    2. Implement a chrome extention to read the text from a page.
    2.2 Use the chrome extention to put the text straight into the NLP.
    3. Take the structured output and make it all the extracted events a pop-up option.
    4. Make the pop-up options editable.
    5. Integrate the pop-up options to the google calendar.

# Environment

Created using uv (https://docs.astral.sh/uv/guides/projects/#creating-a-new-project) a python package and environment manager built in Rust (very fast). Recommended by this article https://nielscautaerts.xyz/python-dependency-management-is-a-dumpster-fire.html

You will need JAVA installed for the Spark NLP package to work