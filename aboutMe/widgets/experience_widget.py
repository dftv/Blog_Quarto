from datetime import date

from IPython.display import Markdown

from .schemas import ExperienceSchema, PositionSchema


def calculateMonths(startDate: date, endDate: date) -> str:
    totalMonths: int = (endDate.year - startDate.year) * 12 + (
        endDate.month - startDate.month + 1
    )

    years, months = divmod(totalMonths, 12)

    return f"{years} years and {months} months" if years > 0 else f"{months} months"


def formatPosition(position: PositionSchema) -> str:
    time: str = calculateMonths(position.startDate, position.endDate)

    startDateFormatted: str = position.startDate.strftime("%B %Y")
    endDateFormatted: str = position.endDate.strftime("%B %Y")

    return (
        f"> > **{position.title}**  \n"
        f"> > {startDateFormatted} - {"Present" if position.present else endDateFormatted} · {time}  \n"
        "> \n"
    )


def generateTitle(experience: ExperienceSchema) -> str:
    firstPosition: PositionSchema = experience.positions[0]

    totalTime: str = calculateMonths(
        experience.positions[-1].startDate, experience.positions[0].endDate
    )

    return (
        f"""> ##### **{experience.company}**  \n"""
        f"> {firstPosition.employmentType.value} · {totalTime}  \n"
        f"> {firstPosition.location} · {firstPosition.locationType.value} \n"
        "> \n"
    )


def experienceWidget(experience: ExperienceSchema) -> Markdown:
    title: str = (
        generateTitle(experience)
        if len(experience.positions) > 1
        else f"""> ##### **{experience.positions[0].title}**\n"""
    )

    content: str = "".join(
        formatPosition(position) for position in experience.positions
    )

    return Markdown(title + content)
