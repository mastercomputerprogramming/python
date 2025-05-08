
def load_csv(filename):
  dataset = list()
  with open(filename,"r") as file:
    csv_reader = reader(file)
    for row in csv_reader:
      if not row:
        continue
      dataset.append(row)
  return dataset

def str_column_to_float(dataset,column):
  for row in dataset:
    row[column]=float(row[column].strip())

def str_column_to_int(dataset,column):
  class_values=[row[column] for row in dataset]
  unique=set(class_values)
  lookup=dict()
  for i, value in enumerate(unique):
    lookup[value] = i
  for row in dataset:
    row[column] = lookup[row[column]]
  return lookup

filename="diabetes.csv"
dataset=load_csv(filename)
for i in range(len(dataset[0])):
  str_column_to_float(dataset,i)

dataset[1]

dataset[2]

def dataset_minmax(dataset):
  minmax=list()
  for i,value in enumerate(dataset):
    col_values = [row for row in value]
    value_min = min(col_values)
    value_max = max(col_values)
    minmax.append([value_min,value_max])
  return minmax

minmax = dataset_minmax(list(dataset[1:]))

def normalize_dataset(dataset,minmax):
  for row in dataset:
    for i,value in enumerate(row):
      if i:
        row[i] = (row[i] - minmax[i][0])/(minmax[i][1]-minmax[i][0])

normalize_dataset(list(dataset[1:]),minmax)

filename="diabetes.csv"
dataset=load_csv(filename)
for i in range(len(dataset[0])):
  str_column_to_float(dataset,i)

def column_means(dataset):
  means = [0 for i  in range(len(dataset[0]))]
  for i,value in enumerate(dataset[0]):
    if i:
      col_values=[row[i] for row in dataset]
      means[i] = sum(col_values)/float(len(dataset))
  return means

def column_stdevs(dataset,means):
  stddevs = [0 for i in range(len(dataset[0]))]
  for i, value in enumerate(dataset[0]):
    variance=[pow(row[i]-means[i],2) for row in dataset]
    stddevs[i]=sum(variance)
  stddevs=[sqrt(x/float(len(dataset)-1)) for x in stddevs]
  return stddevs

means = column_means(dataset[1:])
stddevs = column_stdevs(dataset[1:],means)

def standardize_dataset(dataset,means,stddevs):
  for row in dataset:
    for i in range(len(row)):
      row[i] = (row[i]-means[i])/stddevs[i]

standardize_dataset(dataset[1:],means,stddevs)

dataset[1]

filename="diabetes.csv"
dataset=load_csv(filename)
for i in range(len(dataset[0])):
  str_column_to_float(dataset,i)

def train_test_split(dataset,split=0.60):
  train = list()
  train_size = split * len(dataset)
  dataset_copy = list(dataset)
  while len(train) < train_size:
    index = randrange(len(dataset_copy))
    train.append(dataset_copy.pop(index))
  return train,dataset_copy

train,test = train_test_split(dataset[1:])

print(len(dataset),len(train),len(test))

filename="diabetes.csv"
dataset=load_csv(filename)
for i in range(len(dataset[0])):
  str_column_to_float(dataset,i)

def cross_validation_split(dataset,folds=3):
  dataset_split = list()
  dataset_copy = list(dataset)
  fold_size = int(len(dataset)/folds)
  for i in range(folds):
    fold = list()
    while len(fold) < fold_size:
      index = randrange(len(dataset_copy))
      fold.append(dataset_copy.pop(index))
    dataset_split.append(fold)
  return dataset_split

split_dataset = cross_validation_split(dataset[1:])

len(split_dataset)

[len(i) for i in split_dataset]

def accuracy_metric(actual,predicted):
  correct = 0
  for i in range(len(actual)):
    if actual[i] == predicted[i]:
      correct+=1
  return correct/float(len(actual)) * 100.00

actual = [1,0,0,0,1,1,1,1,1,1]
predicted = [0,1,0,0,0,1,0,1,1,1]
accuracy = accuracy_metric(actual,predicted)
accuracy

def confusion_matrix(actual,predicted):
  unique = set(actual)
  matrix = [list() for x in range(len(unique))]
  for i in range(len(unique)):
    matrix[i] = [0 for x in range(len(unique))]
  lookup = dict()
  for i,value in enumerate(unique):
    lookup[value] = i
  for i in range(len(actual)):
    x=lookup[actual[i]]
    y=lookup[predicted[i]]
    matrix[y][x] +=1
  return unique, matrix

def print_confusion_matrix(unique,matrix):
  print('(A)'+' '.join(str(x) for x in unique))
  print('(P)----')
  for i,x in enumerate(unique):
    print("%s|%s" % (x, ' '.join(str(x) for x in matrix[i])))

unique,matrix = confusion_matrix(actual,predicted)
print_confusion_matrix(unique,matrix)

def mae_metric(actual,predicted):
  sum_error=0.0
  for i in range(len(actual)):
    sum_error+=abs(predicted[i]-actual[i])
  return sum_error/float(len(actual))

actual = [0.1, 0.2, 0.3, 0.4, 0.5]
predicted = [0.11, 0.19, 0.29, 0.41, 0.5]
mae = mae_metric(actual,predicted)

mae

def rmse_metric(actual,predicted):
  sum_error=0.0
  for i in range(len(actual)):
    prediction_error=predicted[i]-actual[i]
    sum_error+=(prediction_error ** 2)
  mean_error = sum_error / float(len(actual))
  return sqrt(mean_error)

actual = [0.1, 0.2, 0.3, 0.4, 0.5]
predicted = [0.11, 0.19, 0.29, 0.41, 0.5]
rmse = rmse_metric(actual,predicted)

rmse

def random_algorithm(train,test):
  output_values = [row[-1] for row in train]
  unique = list(set(output_values))
  predicted = list()
  for _ in test:
    index = randrange(len(unique))
    predicted.append(unique[index])
  return predicted

seed(1)
train = [[0], [1], [0], [1], [0], [1]]
test = [[None], [None], [None], [None]]

predictions = random_algorithm(train,test)

predictions

def zero_rule_algorithm_classification(train,test):
  output_values = [row[-1] for row in train]
  prediction = max(set(output_values),key=output_values.count)
  predicted = [prediction for i in range(len(test))]
  return predicted

seed(1)
train = [['0'], ['0'], ['0'], ['0'], ['1'], ['1']]
test = [[None], [None], [None], [None]]

predictions = zero_rule_algorithm_classification(train,test)

predictions

def zero_rule_algorithm_regression(train,test):
  output_values = [row[-1] for row in train]
  prediction = sum(output_values) / float(len(output_values))
  predicted = [prediction for i in range(len(test))]
  return predicted

seed(1)
train = [[10], [15], [12], [15], [18], [20]]
test = [[None], [None], [None], [None]]

predictions = zero_rule_algorithm_regression(train,test)

predictions

def evaluate_algorithm(dataset,algorithm,split,*args):
  train,test = train_test_split(dataset,split)
  test_set = list()
  for row in test:
    row_copy = list(row)
    row_copy[-1]=None
    test_set.append(row_copy)
  predicted = algorithm(train,test_set,*args)
  actual = [row[-1] for row in test]
  accuracy = accuracy_metric(actual,predicted)
  return accuracy

# Test the train/test harness
seed(1)
# load and prepare data
filename = 'diabetes.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])):
  str_column_to_float(dataset, i)

split = 0.6
accuracy = evaluate_algorithm(dataset[1:],zero_rule_algorithm_classification,split)

print('Accuracy: %.3f%%' % (accuracy))

def evaluate_algorithm_n_fold(dataset,algorithm,n_folds,*args):
  folds = cross_validation_split(dataset,n_folds)
  scores = list()
  for fold in folds:
    train_set = list(folds)
    train_set.remove(fold)
    train_set = sum(train_set,[])
    test_set = list()
    for row in fold:
      row_copy = list(row)
      test_set.append(row_copy)
      row_copy[-1] = None
    predicted = algorithm(train_set,test_set,*args)
    actual = [row[-1] for row in fold]
    accuracy = accuracy_metric(actual,predicted)
    scores.append(accuracy)
  return scores

n_folds = 5
scores = evaluate_algorithm_n_fold(dataset[1:],zero_rule_algorithm_classification,n_folds)
print(f"Scores: {scores}")
print('Mean Accuracy: %.3f%%' % (sum(scores)/len(scores)))

def mean(values):
  return sum(values)/float(len(values))

def variance(values,mean):
  return sum([(x-mean)**2 for x in values])

dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]

x = [row[0] for row in dataset]
y = [row[1] for row in dataset]

mean_x, mean_y = mean(x),mean(y)
var_x, var_y = variance(x,mean_x),variance(y,mean_y)
print('x stats: mean=%.3f variance=%.3f' % (mean_x, var_x))
print('y stats: mean=%.3f variance=%.3f' % (mean_y, var_y))

def covariance(x,mean_x,y,mean_y):
  covar = 0.0
  for i in range(len(x)):
    covar += (x[i] - mean_x) * (y[i] - mean_y)
  return covar

dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
x = [row[0] for row in dataset]
y = [row[1] for row in dataset]
mean_x, mean_y = mean(x), mean(y)
covar = covariance(x, mean_x, y, mean_y)
print('Covariance: %.3f' % (covar))

def coefficients(dataset):
  x = [row[0] for row in dataset]
  y = [row[1] for row in dataset]
  x_mean,y_mean = mean(x), mean(y)
  b1 = covariance(x,mean_x,y,mean_y) / variance(x,x_mean)
  b0 = y_mean - b1 * x_mean
  return [b0, b1]

dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
b0, b1 = coefficients(dataset)
print('Coefficients: B0=%.3f, B1=%.3f' % (b0, b1))

def simple_linear_regression(train, test):
  predictions = list()
  b0, b1 = coefficients(train)
  for row in test:
    yhat = b0 + b1 * row[0]
    predictions.append(yhat)
  return predictions

def evaluate_algorithm_rmse(dataset, algorithm, split, *args):
  train, test = train_test_split(dataset, split)
  test_set = list()
  for row in test:
    row_copy = list(row)
    row_copy[-1] = None
    test_set.append(row_copy)
  predicted = algorithm(train, test_set, *args)
  actual = [row[-1] for row in test]
  rmse = rmse_metric(actual, predicted)
  return rmse

def evaluate_algorithm_rmse_folds(dataset, algorithm, n_folds, *args):
  folds = cross_validation_split(dataset, n_folds)
  scores = list()
  for fold in folds:
    train_set = list(folds)
    train_set.remove(fold)
    train_set = sum(train_set, [])
    test_set = list()
    for row in fold:
      row_copy = list(row)
      test_set.append(row_copy)
      row_copy[-1] = None
  predicted = algorithm(train_set, test_set, *args)
  actual = [row[-1] for row in fold]
  rmse = rmse_metric(actual, predicted)
  scores.append(rmse)
  return scores

dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
rmse = evaluate_algorithm_rmse(dataset, simple_linear_regression,split=0.7)
print('RMSE: %.3f' % (rmse))

seed(1)
# load and prepare data
filename = 'insurance.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])):
  str_column_to_float(dataset, i)

split = 0.6
rmse = evaluate_algorithm_rmse(dataset, simple_linear_regression, split)
print('RMSE: %.3f' % (rmse))

def predict(row,coefficients):
  yhat = coefficients[0]
  for i in range(len(row)-1):
    yhat += coefficients[i+1] * row[i]
  return yhat

dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
coef = [0.4, 0.8]

for row in dataset:
  yhat = predict(row,coef)
  print("Expected=%.3f, Predicted=%.3f" % (row[-1], yhat))

def coefficients_sgd(train,l_rate,n_epoch):
  coef = [0.0 for i in range(len(train[0]))]
  for epoch in range(n_epoch):
    sum_error = 0
    for row in train:
      yhat = predict(row,coef)
      error = yhat - row[-1]
      sum_error += error ** 2
      coef[0] = coef[0] - l_rate * error
      for i in range(len(row) - 1):
        coef[i+1] = coef[i+1] - l_rate * error * row[i]
    print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
  return coef

dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
l_rate = 0.001
n_epoch = 50
coef = coefficients_sgd(dataset,l_rate,n_epoch)
print(coef)

def linear_regression_sgd(train, test, l_rate, n_epoch):
  predictions = list()
  coef = coefficients_sgd(train, l_rate, n_epoch)
  for row in test:
    yhat = predict(row, coef)
    predictions.append(yhat)
  return(predictions)

seed(1)
# load and prepare data
filename = 'winequality-red.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])):
  str_column_to_float(dataset, i)

minmax=dataset_minmax(dataset)
normalize_dataset(dataset,minmax)

# evalueate algorithm
n_folds = 5
l_rate = 0.01
n_epoch = 50
scores = evaluate_algorithm_rmse_folds(dataset, linear_regression_sgd, n_folds, l_rate, n_epoch)
print('Scores: %s' % scores)
print('Mean RMSE: %.3f' % (sum(scores)/float(len(scores))))

from math import exp, pi, sqrt

def predict(row,coefficients):
  yhat = coefficients[0]
  for i in range(len(row)-1):
    yhat += coefficients[i+1] * row[i]
  return 1.0/(1.0+exp(-yhat))

# test predictions
dataset = [[2.7810836,2.550537003,0],
[1.465489372,2.362125076,0],
[3.396561688,4.400293529,0],
[1.38807019,1.850220317,0],
[3.06407232,3.005305973,0],
[7.627531214,2.759262235,1],
[5.332441248,2.088626775,1],
[6.922596716,1.77106367,1],
[8.675418651,-0.242068655,1],
[7.673756466,3.508563011,1]]
coef = [-0.406605464, 0.852573316, -1.104746259]

for row in dataset:
  yhat = predict(row,coef)
  print("Expected=%.3f, Predicted=%.3f [%d]" % (row[-1], yhat, round(yhat)))

def coefficients_sgd(train,l_rate,n_epoch):
  coef=[0.0 for i in range(len(train[0]))]
  for epoch in range(n_epoch):
    sum_error=0
    for row in train:
      yhat = predict(row,coef)
      error=row[-1]-yhat
      sum_error += error ** 2
      coef[0] = coef[0] + l_rate * error * yhat * (1-yhat)
      for i in range(len(row)-1):
        coef[i+1] = coef[i+1] + l_rate * error * yhat * (1-yhat) * row[i]
    print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
  return coef

l_rate = 0.3
n_epoch = 100
coef = coefficients_sgd(dataset, l_rate, n_epoch)
print(coef)

def logistic_regression(train,test,l_rate,n_epoch):
  predictions=list()
  coef=coefficients_sgd(train,l_rate,n_epoch)
  for row in test:
    yhat=predict(row,coef)
    yhat=round(yhat)
    predictions.append(yhat)
  return predictions

def evaluate_algorithm(dataset, algorithm, n_folds, *args):
  folds = cross_validation_split(dataset, n_folds)
  scores = list()
  for fold in folds:
    train_set = list(folds)
    train_set.remove(fold)
    train_set = sum(train_set, [])
    test_set = list()
    for row in fold:
      row_copy = list(row)
      test_set.append(row_copy)
      row_copy[-1] = None
    predicted = algorithm(train_set, test_set, *args)
    actual = [row[-1] for row in fold]
    accuracy = accuracy_metric(actual, predicted)
    scores.append(accuracy)
  return scores

seed(1)
# load and prepare data
filename = 'diabetes.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])):
  str_column_to_float(dataset, i)
# normalize
minmax = dataset_minmax(dataset)
normalize_dataset(dataset, minmax)

n_folds = 5
l_rate = 0.1
n_epoch = 100
scores = evaluate_algorithm(dataset[1:], logistic_regression, n_folds, l_rate, n_epoch)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

def predict(row,weights):
  activation=weights[0]
  for i in range(len(row)-1):
    activation += weights[i+1] * row[i]
  return 1.0 if activation >= 0.0 else 0.0

dataset = [[2.7810836,2.550537003,0],
[1.465489372,2.362125076,0],
[3.396561688,4.400293529,0],
[1.38807019,1.850220317,0],
[3.06407232,3.005305973,0],
[7.627531214,2.759262235,1],
[5.332441248,2.088626775,1],
[6.922596716,1.77106367,1],
[8.675418651,-0.242068655,1],
[7.673756466,3.508563011,1]]
weights = [-0.1, 0.20653640140000007, -0.23418117710000003]

for row in dataset:
  prediction=predict(row,weights)
  print('Expected=%d, Predicted=%d' % (row[-1],prediction))

def train_weights(train,l_rate,n_epoch):
  """
  Psalms 32:8
  I will instruct thee and teach thee in the way which thou shalt go: I will guide thee with mine eye.
  """
  weights = [0.0 for i in range(len(train[0]))]
  for epoch in range(n_epoch):
    sum_error=0.0
    for row in train:
      prediction = predict(row,weights)
      error = row[-1] - prediction
      sum_error += error ** 2
      weights[0] = weights[0] + l_rate * error
      for i in range(len(row)-1):
        weights[i+1]=weights[i+1] + l_rate * error * row[i]
    print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
  return weights

l_rate=0.1
n_epoch = 5
weights = train_weights(dataset,l_rate,n_epoch)
print(weights)

def perceptron(train,test,l_rate,n_epoch):
  predictions=list()
  weights=train_weights(train,l_rate,n_epoch)
  for row in test:
    prediction=predict(row,weights)
    predictions.append(prediction)
  return (predictions)

seed(1)
filename = 'sonar_csv.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])-1):
  str_column_to_float(dataset, i)
# convert string class to integers
str_column_to_int(dataset, len(dataset[0])-1)

n_folds = 3
l_rate = 0.01
n_epoch = 500
scores = evaluate_algorithm(dataset, perceptron, n_folds, l_rate, n_epoch)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

def gini_index(groups,classes):
  n_instances=float(sum([len(group) for group in groups]))
  gini = 0.0

  for group in groups:
    size = float(len(group))
    if size == 0:
      continue
    score = 0.0
    for class_val in classes:
      p=[row[-1] for row in group].count(class_val) / size
      score += p * p
    gini += (1.0 - score) * (size/n_instances)
  return gini

print(gini_index([[[1, 1], [1, 0]], [[1, 1], [1, 0]]], [0, 1]))
print(gini_index([[[1, 0], [1, 0]], [[1, 1], [1, 1]]], [0, 1]))

def test_split(index,value,dataset):
  left,right = list(),list()
  for row in dataset:
    if row[index] < value:
      left.append(row)
    else:
      right.append(row)
  return left,right

def get_split(dataset):
  """get the split"""
  class_values = list(set(row[-1] for row in dataset))
  b_index,b_value,b_score,b_groups = 999,999,999,None
  for index in range(len(dataset[0])-1):
    for row in dataset:
      groups = test_split(index,row[index],dataset)
      gini = gini_index(groups,class_values)
      print('X%d < %.3f Gini=%.3f' % ((index+1), row[index], gini))
      if gini < b_score:
        b_index,b_value,b_score,b_groups = index,row[index],gini,groups
  return {'index':b_index,'value':b_value,'groups':b_groups}

dataset = [[2.771244718,1.784783929,0],
[1.728571309,1.169761413,0],
[3.678319846,2.81281357,0],
[3.961043357,2.61995032,0],
[2.999208922,2.209014212,0],
[7.497545867,3.162953546,1],
[9.00220326,3.339047188,1],
[7.444542326,0.476683375,1],
[10.12493903,3.234550982,1],
[6.642287351,3.319983761,1]]
split = get_split(dataset)
print('Split: [X%d < %.3f]' % ((split['index']+1), split['value']))

def to_terminal(group):
  outcomes = [row[-1] for row in group]
  return max(set(outcomes),key=outcomes.count)

def split(node,max_depth,min_size,depth):
  left,right = node['groups']
  del(node['groups'])

  if not left or not right:
    node['left'] = node['right'] = to_terminal(left+right)
    return

  if depth >= max_depth:
    node['left'],node['right'] = to_terminal(left),to_terminal(right)
    return

  if len(left) <= min_size:
    node['left'] = to_terminal(left)
  else:
    node['left'] = get_split(left)
    split(node['left'],max_depth,min_size,depth+1)

  if len(right) <= min_size:
    node['right'] = to_terminal(right)
  else:
    node['right'] = get_split(right)
    split(node['right'],max_depth,min_size,depth+1)

def build_tree(train, max_depth, min_size):
  root = get_split(train)
  split(root,max_depth,min_size,1)
  return root

def print_tree(node, depth=0):
  if isinstance(node, dict):
    print('%s[X%d < %.3f]' % ((depth*' ', (node['index']+1), node['value'])))
    print_tree(node['left'], depth+1)
    print_tree(node['right'], depth+1)
  else:
    print('%s[%s]' % ((depth*' ', node)))

dataset = [[2.771244718,1.784783929,0],
[1.728571309,1.169761413,0],
[3.678319846,2.81281357,0],
[3.961043357,2.61995032,0],
[2.999208922,2.209014212,0],
[7.497545867,3.162953546,1],
[9.00220326,3.339047188,1],
[7.444542326,0.476683375,1],
[10.12493903,3.234550982,1],
[6.642287351,3.319983761,1]]
tree = build_tree(dataset, 1, 1)
print_tree(tree)

tree = build_tree(dataset, 2, 1)
print_tree(tree)

tree = build_tree(dataset, 3, 1)
print_tree(tree)

def predict(node,row):
  if row[node['index']] < node['value']:
    if isinstance(node['left'],dict):
      return predict(node['left'],row)
    else:
      return node['left']
  else:
    if isinstance(node['right'],dict):
      return predict(node['right'],row)
    else:
      return node['right']

dataset = [[2.771244718,1.784783929,0],
[1.728571309,1.169761413,0],
[3.678319846,2.81281357,0],
[3.961043357,2.61995032,0],
[2.999208922,2.209014212,0],
[7.497545867,3.162953546,1],
[9.00220326,3.339047188,1],
[7.444542326,0.476683375,1],
[10.12493903,3.234550982,1],
[6.642287351,3.319983761,1]]
stump = {'index': 0, 'right': 1, 'value': 6.642287351, 'left': 0}
for row in dataset:
  prediction = predict(stump,row)
  print('Expected=%d, Got=%d' % (row[-1], prediction))

def decision_tree(train,test,max_depth,min_size):
  tree = build_tree(train,max_depth,min_size)
  predictions = list()
  for row in test:
    prediction = predict(tree,row)
    predictions.append(prediction)
  return predictions

seed(1)
# load and prepare data
filename = 'banknote.csv'
dataset = load_csv(filename)
# convert string attributes to integers
for i in range(len(dataset[0])):
  str_column_to_float(dataset, i)

# evaluate algorithm
n_folds = 5
max_depth = 5
min_size = 10
scores = evaluate_algorithm(dataset, decision_tree, n_folds, max_depth, min_size)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

def separate_by_class(dataset):
  separated = dict()
  for i in range(len(dataset)):
    vector = dataset[i]
    class_value = vector[-1]
    if (class_value not in separated):
      separated[class_value] = list()
    separated[class_value].append(vector)
  return separated

dataset = [[3.393533211,2.331273381,0],
[3.110073483,1.781539638,0],
[1.343808831,3.368360954,0],
[3.582294042,4.67917911,0],
[2.280362439,2.866990263,0],
[7.423436942,4.696522875,1],
[5.745051997,3.533989803,1],
[9.172168622,2.511101045,1],
[7.792783481,3.424088941,1],
[7.939820817,0.791637231,1]]
separated = separate_by_class(dataset)

for label in separated:
  print(label)
  for row in separated[label]:
    print(row)

def stdev(numbers):
  avg = mean(numbers)
  variance = sum([(x-avg)**2 for x in numbers])/float(len(numbers)-1)
  return sqrt(variance)

def summarize_dataset(dataset):
  summaries = [(mean(column),stdev(column),len(column)) for column in zip(*dataset)]
  del(summaries[-1])
  return summaries

summary = summarize_dataset(dataset)

summary

def summarize_by_class(dataset):
  separated = separate_by_class(dataset)
  summaries = dict()
  for class_value,rows in separated.items():
    summaries[class_value] = summarize_dataset(rows)
  return summaries

summary = summarize_by_class(dataset)

summary

for label in summary:
  print(label)
  for row in summary[label]:
    print(row)

def calculate_probability(x,mean,stdev):
  exponent = exp(-((x-mean)**2/(2 * stdev**2)))
  return (1/(sqrt(2*pi)*stdev)) * exponent

print(calculate_probability(1.0, 1.0, 1.0))

def calculate_class_probabilities(summaries,row):
  total_rows = sum([summaries[label][0][2] for label in summaries])
  probabilities = dict()
  for class_value,class_summaries in summaries.items():
    probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
    for i in range(len(summaries)):
      mean,stdev,count = class_summaries[i]
      probabilities[class_value] *= calculate_probability(row[i],mean,stdev)
  return probabilities

dataset = [[3.393533211,2.331273381,0],
[3.110073483,1.781539638,0],
[1.343808831,3.368360954,0],
[3.582294042,4.67917911,0],
[2.280362439,2.866990263,0],
[7.423436942,4.696522875,1],
[5.745051997,3.533989803,1],
[9.172168622,2.511101045,1],
[7.792783481,3.424088941,1],
[7.939820817,0.791637231,1]]
summaries = summarize_by_class(dataset)
probabilities = calculate_class_probabilities(summary,dataset[0])

probabilities

def predict(summaries, row):
  probabilities = calculate_class_probabilities(summaries, row)
  best_label, best_prob = None, -1
  for class_value, probability in probabilities.items():
    if best_label is None or probability > best_prob:
      best_prob = probability
      best_label = class_value
  return best_label

def naive_bayes(train,test):
  summarize = summarize_by_class(train)
  predictions = list()
  for row in test:
    output = predict(summarize,row)
    predictions.append(output)
  return predictions

filename = 'Iris.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])-1):
  str_column_to_float(dataset, i)
str_column_to_int(dataset,len(dataset[0])-1)
n_folds = 5
scores = evaluate_algorithm(dataset, naive_bayes, n_folds)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

def euclidean_distance(row1,row2):
  distance = 0.0
  for i in range(len(row1)-1):
    distance += (row1[i]-row2[i])**2
  return sqrt(distance)

dataset = [[2.7810836,2.550537003,0],
[1.465489372,2.362125076,0],
[3.396561688,4.400293529,0],
[1.38807019,1.850220317,0],
[3.06407232,3.005305973,0],
[7.627531214,2.759262235,1],
[5.332441248,2.088626775,1],
[6.922596716,1.77106367,1],
[8.675418651,-0.242068655,1],
[7.673756466,3.508563011,1]]
row0 = dataset[0]
for row in dataset:
  distance = euclidean_distance(row0,row)
  print(distance)

def get_neighbors(train,test_row,num_neighbors):
  distances = list()
  for train_row in train:
    dist = euclidean_distance(test_row,train_row)
    distances.append((train_row,dist))
  distances.sort(key=lambda tup: tup[1])
  neighbors = list()
  for i in range(num_neighbors):
    neighbors.append(distances[i][0])
  return neighbors

dataset = [[2.7810836,2.550537003,0],
[1.465489372,2.362125076,0],
[3.396561688,4.400293529,0],
[1.38807019,1.850220317,0],
[3.06407232,3.005305973,0],
[7.627531214,2.759262235,1],
[5.332441248,2.088626775,1],
[6.922596716,1.77106367,1],
[8.675418651,-0.242068655,1],
[7.673756466,3.508563011,1]]

neighbors=get_neighbors(dataset,dataset[0],3)
for neighbor in neighbors:
  print(neighbor)

def predict_classification(train,test_row,num_neighbors):
  neighbors = get_neighbors(train,test_row,num_neighbors)
  output_values = [row[-1] for row in neighbors]
  prediction = max(set(output_values),key=output_values.count)
  return prediction

prediction = predict_classification(dataset, dataset[0], 3)
print('Expected %d, Got %d.' % (dataset[0][-1], prediction))

def predict_regression(train,test_row,num_neighbors):
  neighbors = get_neighbors(train,test_row,num_neighbors)
  output_values = [row[-1] for row in neighbors]
  prediction = sum(output_values)/float(len(output_values))
  return prediction

def k_nearest_neighbors(train,test,num_neighbors):
  predictions = list()
  for row in test:
    output = predict_classification(train,row,num_neighbors)
    predictions.append(output)
  return predictions

filename="abalone.csv"
dataset = load_csv(filename)
for i in range(1, len(dataset[0])):
  str_column_to_float(dataset, i)
# convert first column to integers
str_column_to_int(dataset, 0)

# evaluate algorithm
n_folds = 5
num_neighbors = 5
scores = evaluate_algorithm(dataset, k_nearest_neighbors, n_folds, num_neighbors)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

def evaluate_algorithm(dataset, algorithm, n_folds, *args):
  folds = cross_validation_split(dataset, n_folds)
  scores = list()
  for fold in folds:
    train_set = list(folds)
    train_set.remove(fold)
    train_set = sum(train_set, [])
    test_set = list()
    for row in fold:
      row_copy = list(row)
      test_set.append(row_copy)
      row_copy[-1] = None
    predicted = algorithm(train_set, test_set, *args)
    actual = [row[-1] for row in fold]
    rmse = rmse_metric(actual, predicted)
    scores.append(rmse)
  return scores

def k_nearest_neighbors(train, test, num_neighbors):
  predictions = list()
  for row in test:
    output = predict_regression(train, row, num_neighbors)
    predictions.append(output)
  return(predictions)

seed(1)
# load and prepare data
filename = 'abalone.csv'
dataset = load_csv(filename)
for i in range(1, len(dataset[0])):
  str_column_to_float(dataset, i)
# convert first column to integers
str_column_to_int(dataset, 0)

# evaluate algorithm
n_folds = 5
num_neighbors = 5
scores = evaluate_algorithm(dataset, k_nearest_neighbors, n_folds, num_neighbors)
print('Scores: %s' % scores)
print('Mean RMSE: %.3f' % (sum(scores)/float(len(scores))))

def get_best_matching_unit(codebooks,test_row):
  distances = list()
  for codebook in codebooks:
    dist = euclidean_distance(codebook,test_row)
    distances.append((codebook,dist))
  distances.sort(key=lambda tup:tup[1])
  return distances[0][0]

# Test best matching unit function
dataset = [[2.7810836,2.550537003,0],
[1.465489372,2.362125076,0],
[3.396561688,4.400293529,0],
[1.38807019,1.850220317,0],
[3.06407232,3.005305973,0],
[7.627531214,2.759262235,1],
[5.332441248,2.088626775,1],
[6.922596716,1.77106367,1],
[8.675418651,-0.242068655,1],
[7.673756466,3.508563011,1]]
test_row = dataset[0]
bmu = get_best_matching_unit(dataset, test_row)
print(bmu)

def random_codebook(train):
  n_records = len(train)
  n_features = len(train[0])
  codebook = [train[randrange(n_records)][i] for i in range(n_features)]
  return codebook

def train_codebooks(train,n_codebooks,lrate,epochs):
  codebooks = [random_codebook(train) for i in range(n_codebooks)]
  for epoch in range(epochs):
    rate = lrate * (1-(epoch/float(epochs)))
    sum_error = 0.0
    for row in train:
      bmu = get_best_matching_unit(codebooks,row)
      for i in range(len(row)-1):
        error=row[i]-bmu[i]
        sum_error += error**2
        if bmu[-1] == row[-1]:
          bmu[i] += rate * error
        else:
          bmu[i] -= rate * error
    print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, rate, sum_error))
  return codebooks

seed(1)
dataset = [[2.7810836,2.550537003,0],
[1.465489372,2.362125076,0],
[3.396561688,4.400293529,0],
[1.38807019,1.850220317,0],
[3.06407232,3.005305973,0],
[7.627531214,2.759262235,1],
[5.332441248,2.088626775,1],
[6.922596716,1.77106367,1],
[8.675418651,-0.242068655,1],
[7.673756466,3.508563011,1]]
learn_rate = 0.3
n_epochs = 10
n_codebooks = 2
codebooks = train_codebooks(dataset, n_codebooks, learn_rate, n_epochs)
print('Codebooks: %s' % codebooks)

def evaluate_algorithm(dataset, algorithm, n_folds, *args):
  folds = cross_validation_split(dataset, n_folds)
  scores = list()
  for fold in folds:
    train_set = list(folds)
    train_set.remove(fold)
    train_set = sum(train_set, [])
    test_set = list()
    for row in fold:
      row_copy = list(row)
      test_set.append(row_copy)
      row_copy[-1] = None
    predicted = algorithm(train_set, test_set, *args)
    actual = [row[-1] for row in fold]
    accuracy = accuracy_metric(actual, predicted)
    scores.append(accuracy)
  return scores

def predict(codebooks,test_row):
  bmu = get_best_matching_unit(codebooks,test_row)
  return bmu[-1]

def learning_vector_quantization(train,test,n_codebooks,lrate,epochs):
  codebooks = train_codebooks(train,n_codebooks,lrate,epochs)
  prediction = list()
  for row in test:
    output = predict(codebooks,row)
    predictions.append(output)
  return predictions

# Test LVQ on Ionosphere dataset
seed(1)
# load and prepare data
filename = 'ionosphere_data_kaggle.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])-1):
  str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)

n_folds = 5
learn_rate = 0.3
n_epochs = 50
n_codebooks = 20
scores = evaluate_algorithm(dataset, learning_vector_quantization, n_folds, n_codebooks,
learn_rate, n_epochs)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

# backpropagation
def initialize_network(n_inputs,n_hidden,n_outputs):
  network = list()
  hidden_layer = [{'weights':[random() for i in range(n_inputs+1)]} for i in range(n_hidden)]
  network.append(hidden_layer)
  output_layer = [{'weights':[random() for i in range(n_hidden+1)]} for i in range(n_outputs)]
  network.append(output_layer)
  return network

seed(1)
network = initialize_network(2,1,2)
for layer in network:
  print(layer)

network

def activate(weights,inputs):
  activation = weights[-1]
  for i in range(len(weights)-1):
    activation += weights[i] * inputs[i]
  return activation

def transfer(activation):
  return 1.0/(1.0+exp(-activation))

def forward_propagate(network,row):
  inputs = row
  for layer in network:
    new_inputs = []
    for neuron in layer:
      activation = activate(neuron['weights'],inputs)
      neuron['output'] = transfer(activation)
      new_inputs.append(neuron['output'])
    inputs = new_inputs
  return inputs

# test forward propagation
network = [[{'weights': [0.13436424411240122, 0.8474337369372327, 0.763774618976614]}],
[{'weights': [0.2550690257394217, 0.49543508709194095]}, {'weights':
[0.4494910647887381, 0.651592972722763]}]]
row = [1, 0, None]
output = forward_propagate(network,row)
print(output)

def transfer_derivative(output):
  return output * (1.0 -output)

def backward_propagate_error(network,expected):
  for i in reversed(range(len(network))):
    layer = network[i]
    errors = list()
    if i!= len(network)-1:
      for j in range(len(layer)):
        error = 0.0
        for neuron in network[i+1]:
          error += (neuron['weights'][j] * neuron.get('delta',0))
        errors.append(error)
    else:
      for j in range(len(layer)):
        neuron = layer[j]
        errors.append(expected[j]-neuron['output'])
    for j in range(len(layer)):
      neuron = layer[i]
      neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])

# test backpropagation of error
network = [[{'output': 0.7105668883115941, 'weights': [0.13436424411240122,
0.8474337369372327, 0.763774618976614]}],
[{'output': 0.6213859615555266, 'weights': [0.2550690257394217, 0.49543508709194095]},
{'output': 0.6573693455986976, 'weights': [0.4494910647887381, 0.651592972722763]}]]

expected = [0,1]
backward_propagate_error(network,expected)
for layer in network:
  print(layer)

def update_weights(network,row,l_rate):
  for i in range(len(network)):
    inputs = row[:-1]
    if i != 0:
      inputs = [neuron['output'] for neuron in network[i]]
    for neuron in network[i]:
      for j in range(len(inputs)):
        neuron['weights'][j] += l_rate * neuron.get('delta',0.0) * inputs[j]
      neuron['weights'][-1] += l_rate * neuron.get('delta',0.0)

def train_network(network,train,l_rate,n_epoch,n_outputs):
  for epoch in range(n_epoch):
    sum_error = 0.0
    for row in train:
      outputs = forward_propagate(network,row)
      expected = [0 for i in range(n_outputs)]
      expected[row[-1]] = 1
      sum_error += sum([(expected[i] - output[i]) ** 2 for i in range(len(expected))])
      backward_propagate_error(network,expected)
      update_weights(network,row,l_rate)
    print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))

seed(1)
dataset = [[2.7810836,2.550537003,0],
[1.465489372,2.362125076,0],
[3.396561688,4.400293529,0],
[1.38807019,1.850220317,0],
[3.06407232,3.005305973,0],
[7.627531214,2.759262235,1],
[5.332441248,2.088626775,1],
[6.922596716,1.77106367,1],
[8.675418651,-0.242068655,1],
[7.673756466,3.508563011,1]]
n_inputs = len(dataset[0]) - 1
n_outputs = len(set([row[-1] for row in dataset]))
network = initialize_network(n_inputs, 2, n_outputs)
train_network(network, dataset, 0.5, 20, n_outputs)

for layer in network:
  print(layer)

def predict(network,row):
  outputs = forward_propagate(network,row)
  return outputs.index(max(outputs))

# Test making predictions with the network
dataset = [[2.7810836,2.550537003,0],
[1.465489372,2.362125076,0],
[3.396561688,4.400293529,0],
[1.38807019,1.850220317,0],
[3.06407232,3.005305973,0],
[7.627531214,2.759262235,1],
[5.332441248,2.088626775,1],
[6.922596716,1.77106367,1],
[8.675418651,-0.242068655,1],
[7.673756466,3.508563011,1]]
network = [[{'weights': [-1.482313569067226, 1.8308790073202204, 1.078381922048799]},
{'weights': [0.23244990332399884, 0.3621998343835864, 0.40289821191094327]}],
[{'weights': [2.5001872433501404, 0.7887233511355132, -1.1026649757805829]}, {'weights':
[-2.429350576245497, 0.8357651039198697, 1.0699217181280656]}]]

for row in dataset:
  prediction = predict(network, row)
  print('Expected=%d, Got=%d' % (row[-1], prediction))

def evaluate_algorithm(dataset, algorithm, n_folds, *args):
  folds = cross_validation_split(dataset, n_folds)
  scores = list()
  for fold in folds:
    train_set = list(folds)
    train_set.remove(fold)
    train_set = sum(train_set, [])
    test_set = list()
    for row in fold:
      row_copy = list(row)
      test_set.append(row_copy)
      row_copy[-1] = None
    predicted = algorithm(train_set, test_set, *args)
    actual = [row[-1] for row in fold]
    accuracy = accuracy_metric(actual, predicted)
    scores.append(accuracy)
  return scores

def train_network(network, train, l_rate, n_epoch, n_outputs):
  for _ in range(n_epoch):
    for row in train:
      forward_propagate(network, row)
      expected = [0 for i in range(n_outputs)]
      expected[round(row[-1])] = 1
      backward_propagate_error(network, expected)
      update_weights(network, row, l_rate)

def backward_propagation(train,test,l_rate,n_epoch,n_hidden):
  n_inputs = len(train[0])-1
  n_outputs = len(set([row[-1] for row in train]))
  network = initialize_network(n_inputs,n_hidden,n_outputs)
  train_network(network,train,l_rate,n_epoch,n_outputs)
  predictions = list()
  for row in test:
    prediction=predict(network,row)
    predictions.append(predict)
  return predictions

# Test Backprop on Seeds dataset
seed(1)
# load and prepare data
filename = 'seeds.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])-1):
  str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)
# normalize input variables
minmax = dataset_minmax(dataset)
normalize_dataset(dataset, minmax)

# evaluate algorithm
n_folds = 5
l_rate = 0.3
n_epoch = 500
n_hidden = 5
scores = evaluate_algorithm(dataset, backward_propagation, n_folds, l_rate, n_epoch, n_hidden)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

def subsample(dataset, ratio=1.0):
  sample = list()
  n_sample = round(len(dataset) * ratio)
  while len(sample) < n_sample:
    index = randrange(len(dataset))
    sample.append(dataset[index])
  return sample

# Test subsampling a dataset
seed(1)
# True mean
dataset = [[randrange(10)] for i in range(20)]
print('True Mean: %.3f' % mean([row[0] for row in dataset]))
# Estimated means
ratio = 0.10
for size in [1, 10, 100]:
  sample_means = list()
  for i in range(size):
    sample = subsample(dataset, ratio)
    sample_mean = mean([row[0] for row in sample])
    sample_means.append(sample_mean)
  print('Samples=%d, Estimated Mean: %.3f' % (size, mean(sample_means)))

def predict(node, row):
  if row[node['index']] < node['value']:
    if isinstance(node['left'], dict):
      return predict(node['left'], row)
    else:
      return node['left']
  else:
    if isinstance(node['right'], dict):
      return predict(node['right'], row)
    else:
      return node['right']

# Make a prediction with a list of bagged trees
def bagging_predict(trees, row):
  predictions = [predict(tree, row) for tree in trees]
  return max(set(predictions), key=predictions.count)

# Bootstrap Aggregation Algorithm
def bagging(train, test, max_depth, min_size, sample_size, n_trees):
  trees = list()
  for _ in range(n_trees):
    sample = subsample(train, sample_size)
    tree = build_tree(sample, max_depth, min_size)
    trees.append(tree)
    predictions = [bagging_predict(trees, row) for row in test]
  return(predictions)

seed(1)
# load and prepare data
filename = 'sonar_csv.csv'
dataset = load_csv(filename)
# convert string attributes to integers
for i in range(len(dataset[0])-1):
  str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)



# evaluate algorithm
n_folds = 5
max_depth = 1
min_size = 2
sample_size = 0.50
for n_trees in [1, 5]:
  scores = evaluate_algorithm(dataset, bagging, n_folds, max_depth, min_size, sample_size,
  n_trees)
  print('Trees: %d' % n_trees)
  print('Scores: %s' % scores)
  print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

# Select the best split point for a dataset
def get_split(dataset, n_features):
  class_values = list(set(row[-1] for row in dataset))
  b_index, b_value, b_score, b_groups = 999, 999, 999, None
  features = list()
  while len(features) < n_features:
    index = randrange(len(dataset[0])-1)
    if index not in features:
      features.append(index)
  for index in features:
    for row in dataset:
      groups = test_split(index, row[index], dataset)
      gini = gini_index(groups, class_values)
      if gini < b_score:
        b_index, b_value, b_score, b_groups = index, row[index], gini, groups
  return {'index':b_index, 'value':b_value, 'groups':b_groups}

# Create child splits for a node or make terminal
def split(node, max_depth, min_size, n_features, depth):
  left, right = node['groups']
  del(node['groups'])
  # check for a no split
  if not left or not right:
    node['left'] = node['right'] = to_terminal(left + right)
    return
  # check for max depth
  if depth >= max_depth:
    node['left'], node['right'] = to_terminal(left), to_terminal(right)
    return
  # process left child
  if len(left) <= min_size:
    node['left'] = to_terminal(left)
  else:
    node['left'] = get_split(left, n_features)
    split(node['left'], max_depth, min_size, n_features, depth+1)
    # process right child
  if len(right) <= min_size:
    node['right'] = to_terminal(right)
  else:
    node['right'] = get_split(right, n_features)
    split(node['right'], max_depth, min_size, n_features, depth+1)

def build_tree(train, max_depth, min_size, n_features):
  root = get_split(train, n_features)
  split(root, max_depth, min_size, n_features, 1)
  return root



def bagging_predict(trees, row):
  predictions = [predict(tree, row) for tree in trees]
  return max(set(predictions), key=predictions.count)

def random_forest(train, test, max_depth, min_size, sample_size, n_trees, n_features):
  trees = list()
  for _ in range(n_trees):
    sample = subsample(train, sample_size)
    tree = build_tree(sample, max_depth, min_size, n_features)
    trees.append(tree)
    predictions = [bagging_predict(trees, row) for row in test]
  return(predictions)

seed(1)
# load and prepare data
filename = 'sonar_csv.csv'
dataset = load_csv(filename)
# convert string attributes to integers
for i in range(len(dataset[0])-1):
  str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)

# evaluate algorithm
n_folds = 5
max_depth = 1
min_size = 1
sample_size = 1.0
n_features = int(sqrt(len(dataset[0])-1))
for n_trees in [1, 5]:
  scores = evaluate_algorithm(dataset, random_forest, n_folds, max_depth, min_size,
  sample_size, n_trees, n_features)
  print('Trees: %d' % n_trees)
  print('Scores: %s' % scores)
  print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

def knn_model(train):
  return train

# Make a prediction with KNN
def knn_predict(model, test_row, num_neighbors=2):
  neighbors = get_neighbors(model, test_row, num_neighbors)
  output_values = [row[-1] for row in neighbors]
  prediction = max(set(output_values), key=output_values.count)
  return prediction

def perceptron_predict(model, row):
  activation = model[0]
  for i in range(len(row)-1):
    activation += model[i + 1] * row[i]
  return 1.0 if activation >= 0.0 else 0.0

def perceptron_model(train, l_rate=0.01, n_epoch=5000):
  weights = [0.0 for i in range(len(train[0]))]
  for epoch in range(n_epoch):
    for row in train:
      prediction = perceptron_predict(weights, row)
      error = row[-1] - prediction
      weights[0] = weights[0] + l_rate * error
      for i in range(len(row)-1):
        weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
  return weights

def logistic_regression_predict(model, row):
  yhat = model[0]
  for i in range(len(row)-1):
    if model[i+1] and row[i]:
      yhat += model[i + 1] * row[i]
  return 1.0 / (1.0 + exp(-yhat))

def logistic_regression_model(train, l_rate=0.01, n_epoch=5000):
  coef = [0.0 for i in range(len(train[0]))]
  for epoch in range(n_epoch):
    for row in train:
      yhat = logistic_regression_predict(coef, row)
      error = row[-1] - yhat if row[-1] else 0.0
      coef[0] = coef[0] + l_rate * error * yhat * (1.0 - yhat)
      for i in range(len(row)-1):
        coef[i + 1]
  return coef

def to_stacked_row(models, predict_list, row):
  stacked_row = list()
  for i in range(len(models)):
    prediction = predict_list[i](models[i], row)
    stacked_row.append(prediction)
    stacked_row.append(row[-1])
  return row[0:len(row)-1] + stacked_row

# Stacked Generalization Algorithm
def stacking(train, test):
  model_list = [knn_model, perceptron_model]
  predict_list = [knn_predict, perceptron_predict]
  models = list()
  for i in range(len(model_list)):
    model = model_list[i](train)
    models.append(model)
    stacked_dataset = list()
  for row in train:
    stacked_row = to_stacked_row(models, predict_list, row)
    stacked_dataset.append(stacked_row)
    stacked_model = logistic_regression_model(stacked_dataset)
    predictions = list()
  for row in test:
    stacked_row = to_stacked_row(models, predict_list, row)
    stacked_dataset.append(stacked_row)
  stacked_model = logistic_regression_model(stacked_dataset)
  predictions = list()
  for row in test:
    stacked_row = to_stacked_row(models, predict_list, row)
    stacked_dataset.append(stacked_row)
    prediction = logistic_regression_predict(stacked_model, stacked_row)
    prediction = round(prediction)
    predictions.append(prediction)
  return predictions

# load and prepare data
filename = 'sonar_csv.csv'
dataset = load_csv(filename)
# convert string attributes to integers
for i in range(len(dataset[0])-1):
  str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)

n_folds = 2
scores = evaluate_algorithm(dataset, stacking, n_folds)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

# completion

# prompt: a python function that performs backpropagation

def backpropagation(network, row, l_rate):
  outputs = forward_propagate(network,row)
  expected = [0 for i in range(len(network[-1]))]
  expected[row[-1]] = 1
  for i in reversed(range(len(network))):
    layer = network[i]
    errors = list()
    if i != len(network)-1:
      for j in range(len(layer)):
        error = 0.0
        for neuron in network[i+1]:
          error += (neuron['weights'][j] * neuron.get('delta',0))
        errors.append(error)
    else:
      for j in range(len(layer)):
        neuron = layer[j]
        errors.append(expected[j]-neuron['output'])
    for j in range(len(layer)):
      neuron = layer[i]
      neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])
      for k in range(len(neuron['weights'])):
        neuron['weights'][k] += l_rate * neuron.get('delta',0.0) * input[k]
      neuron['weights'][-1] += l_rate * neuron.get('delta',0.0)


