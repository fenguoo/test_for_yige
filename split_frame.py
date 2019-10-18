def spilt_frame(file_path=None):
    with open(file_path, 'r') as f:
        pred = f.readlines()
    # import pdb;pdb.set_trace()
    pred_dict = {}
    for i in range(len(pred)):
        if not pred[i].split(' ')[0] in pred_dict:
            pred_dict[pred[i].split(' ')[0]] = [pred[i].split('\n')[0].split(' ')[1:]]
        else:
            pred_dict[pred[i].split(' ')[0]].append(pred[i].split('\n')[0].split(' ')[1:])
    for frame_id in pred_dict.keys():
        save_name = file_path[:-4] + '_frame_%s'%(frame_id) + file_path[-4:]
        write_new_result(frame_id=frame_id, pred=pred_dict[frame_id], save_name=save_name)
    import pdb;pdb.set_trace()

def write_new_result(frame_id, pred, save_name):
    with open(save_name, 'w') as f:
        for i in range(len(pred)):
            f.write('%s %s %s %s %s\n' % (frame_id, pred[i][0], pred[i][1], pred[i][2], pred[i][3]))
    f.close()

if __name__ == '__main__':
    txt_path = './test.txt'
    pred_dict = spilt_frame(file_path=txt_path)
