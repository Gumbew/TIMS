import pearson as pr
import plots as p
from sample import DiscreteSample
from stats import SampleStats


def main():
    sample = DiscreteSample(a=1, b=12, amount=10)

    p.print_histogram(sample.w_table)
    p.print_plot(sample.freq_table)

    print(pr.pearson(sample))

    stats = SampleStats(sample)
    stats.print()


main()
