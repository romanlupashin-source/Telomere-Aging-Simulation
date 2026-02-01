import random
import matplotlib.pyplot as plt


def simulate_normal_cell(start_length, critical_limit, max_divisions):
    """
    Simulate telomere shortening in a normal somatic cell.
    """
    telomere = start_length
    history = [telomere]

    for _ in range(max_divisions):
        loss = random.randint(50, 150)
        telomere -= loss

        if telomere <= critical_limit:
            history.append(critical_limit)
            break

        history.append(telomere)

    return history


def simulate_cancer_cell(start_length, max_divisions):
    """
    Simulate telomere dynamics in a cancer cell with active telomerase.
    """
    telomere = start_length
    history = [telomere]

    for _ in range(max_divisions):
        loss = random.randint(50, 150)
        growth = random.randint(50, 150)
        telomere = telomere - loss + growth
        history.append(telomere)

    return history


def plot_results(normal_history, cancer_history, critical_limit):
    """
    Visualize telomere dynamics.
    """
    plt.figure(figsize=(10, 6))

    plt.plot(
        normal_history,
        label="Normal cell (Somatic)",
        color="blue",
        linewidth=2
    )

    plt.plot(
        cancer_history,
        label="Cancer cell (Telomerase active)",
        color="red",
        linewidth=2
    )

    plt.axhline(
        y=critical_limit,
        color="black",
        linestyle="--",
        label="Hayflick limit"
    )

    plt.title("Telomere Dynamics: Aging vs Immortality")
    plt.xlabel("Cell divisions (Generations)")
    plt.ylabel("Telomere length (bp)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
plt.savefig("results.png", dpi=150)
plt.show()


if __name__ == "__main__":
    # Simulation parameters
    START_LENGTH = 10_000
    CRITICAL_LIMIT = 500
    MAX_DIVISIONS = 100

    normal = simulate_normal_cell(
        START_LENGTH, CRITICAL_LIMIT, MAX_DIVISIONS
    )

    cancer = simulate_cancer_cell(
        START_LENGTH, MAX_DIVISIONS
    )

    plot_results(normal, cancer, CRITICAL_LIMIT)
