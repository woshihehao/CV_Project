1. conda install -c menpo cyvlfeat 最好使用conda来安装依赖，pip不好编译cyvlfeat库
2. python proj3.py 随机15类选择1类 正确率1/15 7%左右
   python proj3.py --feature tiny_image --classifier nearest_neighbor 采用tiny_image特征最近邻分类 accuracy of about 20%
   python proj3.py --feature bag_of_sift --classifier nearest_neighbor 采用sift特征最近邻分类 accuracy of about 50%
   python proj3.py --feature bag_of_sift --classifier support_vector_machine 采用sift特征SVM分类 accuracy of about 60%