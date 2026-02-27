from datetime import datetime, date

BIRTH_DATE = date(1997, 7, 7)
LIFE_EXPECTANCY_YEARS = 100


def calculate_life_progress():
    today = date.today()
    end_date = date(BIRTH_DATE.year + LIFE_EXPECTANCY_YEARS, 7, 7)

    days_lived = (today - BIRTH_DATE).days
    total_days = (end_date - BIRTH_DATE).days
    days_remaining = total_days - days_lived

    percentage = (days_lived / total_days) * 100

    return days_lived, days_remaining, percentage


def progress_bar(percentage):
    total_blocks = 30
    filled_blocks = int((percentage / 100) * total_blocks)
    empty_blocks = total_blocks - filled_blocks

    return "█" * filled_blocks + "░" * empty_blocks


def generate_markdown():
    today = datetime.now().strftime("%d/%m/%Y")
    days_lived, days_remaining, percentage = calculate_life_progress()
    bar = progress_bar(percentage)

    content = f"""# 🕯 Memento Mori — {today}

Nascimento: 07/07/1997  
Expectativa: 100 anos  

Idade: {int(days_lived / 365.25)} anos  
Dias vividos: {days_lived}  
Dias restantes: {days_remaining}  
Vida completada: {percentage:.2f}%

Progresso:
{bar} {percentage:.0f}%

"Construa algo hoje que sobreviva ao tempo."
"""

    with open("life_progress.md", "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    generate_markdown()