import random
import matplotlib.pyplot as plt  

def monte_carlo_pi(num_samples: int) -> float:
    inside_circle = 0
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return 4 * inside_circle / num_samples

if __name__ == "__main__":
    samples = 1000000   
    pi_estimate = monte_carlo_pi(samples)
    print(f"Estimated value of Pi after {samples} samples: {pi_estimate}")

    estimates = []
    inside_circle = 0
    for i in range(1, samples + 1):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
        if i % 1000 == 0:  
            estimates.append(4 * inside_circle / i)

    plt.plot(range(1000, samples + 1, 1000), estimates)
    plt.axhline(y=3.141592653589793, color='r', linestyle='--', label='Actual Pi')
    plt.xlabel('Number of Samples')
    plt.ylabel('Estimated Pi')
    plt.title('Monte Carlo Estimation of Pi')
    plt.legend()
    plt.show()