import Levenshtein
from tqdm import tqdm

def compare_packets_dist(fake_array, real_array, lev_dists):
    i=0
    for fp in tqdm(fake_array):
        for rp in real_array:
            dist = Levenshtein.distance(fp, rp)

            if dist<=lev_dists[i][1]:
                if dist==lev_dists[i][1]:
                    lev_dists[i][3]+=1
                else:
                    lev_dists[i][1]=dist
                    lev_dists[i][2]=rp
        i+=1

    return lev_dists

def compare_packets_ratio(fake_array, real_array, ratios):
    i=0
    for fp in tqdm(fake_array):
        for rp in real_array:
            ratio = Levenshtein.ratio(fp, rp)

            if ratio>=ratios[i][1]:
                if ratio==ratios[i][1]:
                    ratios[i][3]+=1
                else:
                    ratios[i][1]=ratio
                    ratios[i][2]=rp
        i+=1

    return ratios