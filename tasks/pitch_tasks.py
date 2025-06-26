# tasks/pitch_tasks.py
from crewai import Task
from agents.pitch_analyst import pitch_analyst
from agents.domain_advisor import domain_advisor

from agents.rewriter import rewriter

def get_tasks(pitch_text, domain):
    return [
        Task(
            description=f"Analyze this startup pitch: {pitch_text}",
            expected_output="Point out clarity issues, vague sections, and what slides are missing.",
            agent=pitch_analyst
        ),
        Task(
            description=f"Provide suggestions and domain-specific trends for {domain}",
            expected_output=f"Include industry-specific feedback for {domain}",
            agent=domain_advisor
        ),
        Task(
            description="Rewrite the full pitch using feedback from the above steps.",
            expected_output="A clean, investor-ready pitch in markdown format.",
            agent=rewriter,
            output_file="outputs/rewritten_pitch.md"
        )
    ]
