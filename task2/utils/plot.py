import matplotlib.pyplot as plt
import seaborn as sns
import utils.localization as localization
import utils.proximity as proximity


def get_disease_module_info(dis_name, gda, gppi, print_info=False):
    d = gda[gda.diseaseName == dis_name]
    genes = list(d.geneSymbol.unique())
    genes_in_ppi = [n for n in gppi.nodes if n in genes]
    genes_in_lcc = localization.get_lcc(gppi, genes_in_ppi)

    if print_info:
        print("Disease: ", dis_name)
        print("Number of disease genes: ", len(genes))
        print("Number of disease genes in the PPI: ", len(genes_in_ppi))
        print("Number of disease genes in the LCC: ", len(genes_in_lcc))

    return genes, genes_in_ppi, genes_in_lcc


def plot_disease_module_info(ppi, genes):
    sig_dict = localization.get_random_comparison(ppi, genes[1], 1000)
    random_lcc = sig_dict["LCC_list"]

    print("Full randomization")
    print("Mean: ", sig_dict["mean"])
    print("Std: ", sig_dict["std"])
    print("z-score: ", sig_dict["z_score"])
    print("p-value: ", sig_dict["p_value"])

    sig_dp_dict = localization.get_random_comparison(
        ppi, genes[1], 1000, degree_preserving=True
    )
    random_dp_lcc = sig_dp_dict["LCC_list"]

    print("\nDegree preserving randomization")
    print("Mean: ", sig_dp_dict["mean"])
    print("Std: ", sig_dp_dict["std"])
    print("z-score: ", sig_dp_dict["z_score"])
    print("p-value: ", sig_dp_dict["p_value"], "\n")

    sns.set_style("whitegrid")
    _, axs = plt.subplots(1, 2, figsize=(12, 4))

    sns.histplot(data=random_lcc, bins=10, ax=axs[0])
    axs[0].axvline(len(genes[2]), color="r")
    axs[0].set_xlabel("LCC Value")
    axs[0].set_ylabel("Iterations Count")
    axs[0].set_title("Full Randomization")

    sns.histplot(data=random_dp_lcc, bins=10, ax=axs[1])
    axs[1].axvline(len(genes[2]), color="r")
    axs[1].set_xlabel("LCC Value")
    axs[1].set_ylabel("Iterations Count")
    axs[1].set_title("Degree Preserving Randomization")

    plt.tight_layout()
    plt.show()


def plot_proximity(G, genes, targets, sim):
    prox_dict = proximity.get_proximity(G, genes, targets, sim)

    prox_obs = prox_dict["proximity"]
    random_prox = prox_dict["proximity_list"]

    print("Proximity observed: ", prox_obs)
    print("\nMean: ", prox_dict["mean"])
    print("Std: ", prox_dict["std"])
    print("z-score: ", prox_dict["z_score"])
    print("p-value: ", prox_dict["p_value"])

    sns.set_style("whitegrid")
    sns.histplot(data=random_prox, bins=10)
    plt.axvline(prox_obs, color="r")
    plt.title("Proximity Value Distribution", fontsize=16, fontweight="bold")
    plt.xlabel("Proximity Value")
    plt.ylabel("Count Iterations")
    plt.tight_layout()
    plt.show()


def plot_separation_value_histogram(sorted_df):
    sns.set_style("whitegrid")
    plt.figure(figsize=(8, 6))
    sns.histplot(sorted_df["Separation"], bins=30, kde=True)
    plt.title("Separation Value Distribution", fontsize=16, fontweight="bold")
    plt.xlabel("Separation Value")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
