import numpy as np
# from collections import defaultdict

if __name__ == '__main__':
    datasets = ['Yelp', 'Gowalla']
    samplings = [100]
    models = ['GeoSoCa', 'LORE', 'CF', 'PFM']
    top_n = [5, 10, 20]
    for dataset in datasets:
        for sampling in samplings:
            for model in models:
                if model in ['CF', 'PFM']:
                    fusions = ['main']
                elif dataset== 'Gowalla' and model == 'GeoSoCa':
                    fusions = ['mul', 'sum', 'local', 'local_1', 'local_2', 'local_3', 'w19', 'w37', 'w55', 'w73', 'w91']
                else:
                    fusions = ['mul', 'sum', 'local', 'local_1', 'local_2', 'local_3', 'mul', 'sum', 'local', 'w117', 'w144', 'w171', 'w333', 'w414', 'w441', 'w711']
                for fusion in fusions:
                    path = "results/" + dataset + "/" + model + "/" + model + "_" + fusion + "/"
                    # ['all', 'leisure', 'working', 'active', 'inactive']
                    user_groups = ['all', 'leisure', 'working']
                    for user_group in user_groups:
                        # load user group data: all, active, inactive, leisure, working
                        users_ids = set()
                        with open(f'./groups/user_groups/{dataset}/{user_group}.txt','r') as user_group_data:
                            for uid in user_group_data.readlines():
                                users_ids.add(uid.strip())

                        for topN in top_n:
                            all_precision, all_recall, all_nDCG, all_MAP, all_novel, all_diversity = [], [], [], [], [], []
                            result_file = open(path + "result_top_" + str(topN) + ".txt", 'r')
                            result_data = result_file.readlines()
                            for eachline in result_data:
                                cnt, uid, precision, recall, nDCG, MAP, novel, diversity = eachline.strip().split('\t')
                                precision, recall, MAP, NDCG = float(precision), float(recall), float(MAP), float(nDCG)
                                if uid in users_ids:
                                    all_precision.append(precision)
                                    all_recall.append(recall)
                                    all_MAP.append(MAP)
                                    all_nDCG.append(NDCG)

                            final_results = open(path + "result_mean_" + str(topN) + "_" + user_group + ".txt", 'w')
                            final_results.write("Precision\tRecall\tMAP\tNDCG\n")
                            final_results.write('\t'.join([str(round(np.mean(all_precision), 4)), str(round(np.mean(all_recall), 4)), str(round(np.mean(all_MAP), 4)), str(round(np.mean(all_nDCG), 4))]) + '\n')

                            result_file.close()
                            result_data.clear()
