from IPython.display import Markdown

from .schemas import EducationSchema


def educationWidget(education: EducationSchema) -> Markdown:
    title: str = f"""> ##### **{education.degree}**\n"""

    startDateFormatted: str = education.startDate.strftime("%B %Y")
    endDateFormatted: str = education.endDate.strftime("%B %Y")

    content: str = (
        f"> > {education.institution},  \n"
        f"> > {startDateFormatted} - {"Current" if education.present else  endDateFormatted}  \n"
        "> \n"
    )

    return Markdown(title + content)
