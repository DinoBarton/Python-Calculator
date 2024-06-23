def get_project_scores(projects, criteria_weights):
    project_scores = {}
    
    for project, criteria in projects.items():
        total_score = 0
        for criterion, weight in criteria_weights.items():
            total_score += criteria[criterion] * weight
        project_scores[project] = total_score
    
    return project_scores

def decide_project(project_scores):
    return max(project_scores, key=project_scores.get)

projects = {
    "Book": {"Urgency": 2, "Impact": 5, "Interest": 4, "Resources Required": 1, "Skills Development": 2},
    "Company": {"Urgency": 2, "Impact": 5, "Interest": 5, "Resources Required": 4, "Skills Development": 4}
}

criteria_weights = {"Urgency": 0.30, "Impact": 0.25, "Interest": 0.20, "Resources Required": -0.15, "Skills Development": 0.10}

project_scores = get_project_scores(projects, criteria_weights)

best_project = decide_project(project_scores)

print(f"The best project to work on is: {best_project}")
