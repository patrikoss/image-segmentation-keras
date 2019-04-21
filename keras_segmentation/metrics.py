import numpy as np
import keras.backend as K

EPS = 1e-12

def mean_acc(y_true, y_pred):
	import ipdb; ipdb.set_trace()
	print(y_true.shape, y_pred.shape, y_pred, y_true)
	mask0 = y_true[:, :, 0] == 1.0
	zeros = K.sum(mask0)
	mask1 = y_true[:,:,1] == 1.0
	ones = K.sum(mask1)
	pred_cls = K.round(y_pred)
	return mask1 * K.equal(pred_cls[:,:,1], y_true[:,:,1]) / ones + \
		   mask0 * K.equal(pred_cls[:,:,0], y_true[:,:,0]) / zeros

	# true_cases = K.sum(y_true)
	# true_positives = K.equal(
	# 	K.cast(
	# 		K.equal(K.round(y_pred), y_true),
	# 		K.floatX
	# 	), 1.0
	# )



def get_iou( gt , pr , n_classes ):
	class_wise = np.zeros(n_classes)
	for cl in range(n_classes):
		intersection = np.sum(( gt == cl )*( pr == cl ))
		union = np.sum(np.maximum( ( gt == cl ) , ( pr == cl ) ))
		iou = float(intersection)/( union + EPS )
		class_wise[ cl ] = iou
	return class_wise
