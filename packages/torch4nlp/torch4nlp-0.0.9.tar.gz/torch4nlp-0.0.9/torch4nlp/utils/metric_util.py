def cal_prf1(cnt_tp, cnt_pred, cnt_truth, eps=1e-8):
    precision = cnt_tp / (cnt_pred + eps)
    recall = cnt_tp / (cnt_truth + eps)
    f1 = 2*cnt_tp / (cnt_pred + cnt_truth + 1e-8)
    return 100*precision, 100*recall, 100*f1

