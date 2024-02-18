# from include import *
# from data import *
# import builtins
# from Cope import debug
# data = pd.read_csv('https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/cereal.csv')
# For when we need a lot of samples
# bigData = pd.read_csv('https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/bikes.csv')

# relevant = ('mfr', 'fat', 'calories', 'name', 'rating')
# target = 'rating'
'''
def split(*data, amt:Union[int, float, Iterable[Union[int, float]]]=.2, method:Union[Literal['random', 'head', 'tail'], Iterable[Literal['train', 'test']]]='random', target=[], splitTargets=False, seed=42):
    """ Splits the given data, both into train/test sets, and by taking out targets at the same time
        `target` can be a string or an iterable
        If `splitTargets` is set to False, the targets will always return DataFrames, even if
            they only have 1 column
        If you pass in multiple items for data, AND specify a target feature[s], then all the items
            must have the target columns
        The order goes:
            train_X, test_X, train_X1, test_X1, ..., train_y, test_y, train_y1, test_y1
            where it continues adding data and target splits in the order they are given.
            Simply put, it outputs in the same order you input the parameters as much as possible.
            Don't give multiple data AND split targets at the same time. While it can do it,
                it's simply too confusing to think through the order of the returned parameters.
        Setting the `method` to 'chunk' is the same as setting it to 'tail'.
    """
    if len(ensureIterable(data)) > 1 and len(target):
        warn("Please don't give multiple data AND split targets at the same time. While it can do it, "
             "it's simply too confusing to think through the order of the returned parameters.")
    # Pop the targets and combine everything into 1 ordered list of things we need to split
    splitMe = []
    for d in ensureIterable(data):
        d = d.copy()

        targets = [d.pop(t) for t in ensureIterable(target)]
        if splitTargets:
            splitMe += targets
        else:
            splitMe.append(pd.DataFrame(dict(zip(ensureIterable(target), targets))))
        # It makes more sense to do data, then target, not target then data
        splitMe.insert(0 if len(targets) else len(splitMe), d)

    # Now split everything in the list (order is important!)
    if method == 'random':
        disp(splitMe)
        return skms.train_test_split(*splitMe, test_size=amt, random_state=seed)
    elif method in ('head', 'tail', 'chunk'):
        rtn = []
        for d in splitMe:
            # Head an tail splitting are the same, just with opposite amts
            split = round(len(d) * (amt if method == 'head' else (1-amt)))
            rtn += [d.iloc[:split], d.iloc[split:]]
        return rtn
    else:
        raise TypeError(f"Invalid method parameter given")
# train_X, test_X, train_X1, test_X1, ..., train_y, test_y, train_y1, test_y1
_testSize = len(data) * .2
_trainSize = len(data) * .8
_test_data, _train_data = skms.train_test_split(data, test_size=.2, random_state=42)

try:
    split(data, amt=[.2])
except: print('success')
else: print('failed to throw error')
try:
    split(data, amt=(.6), method=('train', 'test', 'train'))
except: print('success')
else: print('failed to throw error')
try:
    split(data, amt=(.2, .6), method=('train', 'test'))
except: print('success')
else: print('failed to throw error')

# split(data, amt=(.2, .6), method=('train', 'test', 'train'))
# split(data, amt=[.2], method=('train', 'test'))
# split(data, amt=.2, method='tail')
# split(data, amt=.2, method='head')
split(data, amt=.2, method='random')

# # split(data, amt=(.2, .6), method=('train', 'test', 'train'), target='mfr')
# # split(data, amt=[.2], method=('train', 'test'), target='mfr')
# split(data, amt=.2, method='tail', target='mfr')
# split(data, amt=.2, method='head', target='mfr')
# split(data, amt=.2, method='random', target='mfr')

# # split(data, amt=(.2, .6), method=('train', 'test', 'train'), target=['mfr', 'fat'])
# # split(data, amt=[.2], method=('train', 'test'), target=['mfr', 'fat'])
# split(data, amt=.2, method='tail', target=['mfr', 'fat'])
# split(data, amt=.2, method='head', target=['mfr', 'fat'])
# split(data, amt=.2, method='random', target=['mfr', 'fat'])

# # split(data, amt=(.2, .6), method=('train', 'test', 'train'), target=['mfr', 'fat'], splitTargets=True)
# # split(data, amt=[.2], method=('train', 'test'), target=['mfr', 'fat'], splitTargets=True)
# split(data, amt=.2, method='tail', target=['mfr', 'fat'], splitTargets=True)
# split(data, amt=.2, method='head', target=['mfr', 'fat'], splitTargets=True)
# split(data, amt=.2, method='random', target=['mfr', 'fat'], splitTargets=True)





from include import *
from data import *
import builtins
from sklearn.preprocessing import MinMaxScaler
# import deepreload
from Cope import debug
%load_ext autoreload
data = pd.read_csv('https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/cereal.csv')
# For when we need a lot of samples
bigData = pd.read_csv('https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/bikes.csv')


relevant = ('mfr', 'fat', 'calories', 'name', 'rating')
target = 'rating'

%autoreload 2
explore(data)
# len(data)


# print('Before decorator defined')
def decorator(decorator_arg, decorator_kwarg=None):
    # print('Called when decorator is added')
    # print('params are:', decorator_arg)
    def outer(decorator_func):
        # print('Also called when decorator is added?')
        @wraps(decorator_func)
        def inner(*args, **kwargs):
            # print('Called when func is. params are:', args)
            rtn = decorator_func(*args, **kwargs)
            return rtn
        return inner
    return outer
# print('After decorator defined')

# print('Before func defined')
@decorator(30.0, 'foobarbaz')
def func(a, b, c):
    # print('Just inside func')
    return a + b + c
# print('After func defined')


# print('Before func called')
func(1, 2, 3)
# print('After func called')

def decorator(decorator_arg, decorator_kwarg=None):
    # Runs when the decorator is added
    def outer(decorator_func):
        # Also runs when the decorator is added
        # This decorator just helps the interpreter know what's what
        @wraps(decorator_func)
        def inner(*args, **kwargs):
            # Runs when the decorated function gets called
            rtn = decorator_func(*args, **kwargs)
            return rtn
        return inner
    return outer

@decorator(30.0, 'foobarbaz')
def func(a, b, c):
    return a + b + c

func(1, 2, 3,)

@_cleaningFunc(df=pd.DataFrame)
def func(df, log=...):
    log(type(df))
    display(df)

func((data.mfr, ), verbose=True)


%autoreload 2
# disp(split(data, amt=.1, target=['rating', 'weight']))
rating = data.copy().pop('rating')
# disp(split(data, rating, amt=.1))
# a, b = split(data, method='tail', amt=.5, splitTargets=True)
# disp((a, b))
disp(split(data, amt=.1, method='random', target=['rating', 'weight', 'sodium', 'fat'], splitTargets=True))
# display(a)
# display(b)

# train_X_a, test_X_a, train_y, test_y, train_y1, test_y1, train_X1, test_X1,

# data['date'] = parse_date(data.dteday)
# convert_time(data)
# data

# _data = convert_numeric(data.drop(columns=['name']))
# normalize(_data)


# handle_outliers
# handle_missing
# remove
# bin
%autoreload 2
# data = convert_numeric(data.mfr, col=None, method='one_hot_encode')
# data
# rescale()
d = bigData.drop(columns=['dteday'])
rescale(df=split(d, amt=.2, method='chunk'))
# d



%autoreload 2
col = data['sodium']
# handle_outliers(col, method='remove', zscore=1, verbose=True)
# print(data.mfr)
# print(data.rating)
# handle_outliers(col, method='constrain', zscore=3, verbose=True)
# handle_missing(col, np.nan, missing_value=200, verbose=True)
# handle_missing(col, method:Union[Series, 'remove', 'mean', 'median', 'mode', 'random', 'balanced_random', Any], missing_value=np.nan, verbose=True)
# query(data, 'sodium', 'sodium > 200', 4, verbose=True)
# query(df:pd.DataFrame, column:str, query:str, method:Union[Series, 'remove', 'mean', 'median', 'mode', 'random', 'balanced_random', Any], verbose=True)
# query(data, 'healthy', 'fat < 3 & calories < 100', 'new', false='unhealthy', true='healthy')
# remove(col, 200, verbose=True)
# bin(col, (0, 90, 150, 1000), amt=5, verbose=True)
# bin(col, method:Union['frequency', 'width', Tuple, List], amt=5, verbose=True)
# normalize(col, verbose=True)
# convert_numeric(data, 'sodium', method:Union['assign', 'one_hot_encode']='one_hot_encode', returnAssignments=False, verbose=True)
# convert_numeric(data, method='one_hot_encode', returnAssignments=False, verbose=True)


%autoreload 2
explore(data, target=target, start='Description', startFeature=None)
# quantitative(data)

pd.Series(pd.Series([1, 2, 3], name='a'), name='b')





%autoreload 2
''
config = {
    # Do these to all the columns, or a specified column
    'all': {
        # If provided, specifies a method by which to convert a catagorical feature to a quantative one
        'drop_duplicates': True,
        'normalize': 'min-max',
        'convert_numeric': 'one_hot_encode',
        # If provided, specifies a method by which to normalize the quantative values
        # Drop duplicate samples
        # If provided, specifies a value that is equivalent to the feature being missing
        # 'missing_value': Any,
        # If provided, specifies a method by which to transform samples with missing features
        # 'handle_missing': Union[bool, 'remove', 'mean', 'median', 'mode', Any],
        # If provided, specifies a method by which to bin the quantative value, or specify custom ranges
        # 'bin': Union[bool, Tuple['frequency', int], Tuple['width', int], Iterable],
        # If provided, maps feature values to a dictionary
        # 'map': Union[bool, Dict],
        # If provided, removes all samples with the given value
        # 'remove': Union[bool, Any],
        # If provided, applies a function to the column
        # 'apply': Union[bool, Callable],
        # A ndarray of shape (1, n) of bools to apply to the column to create a new column with the given name
        # Usable on single columns only (not all)
        # 'create_new': Tuple[str, np.ndarray],
    },
    'calories': {
        # 'drop_duplicates': False,
        'missing_value': 70,
        'handle_missing': 'mean',
        # 'normalize': 'range',
        'bin': ('frequency', 7),
        # 'map': Union[bool, Dict],
        # 'remove': True,
        'convert_numeric': 'assign',
        # 'apply': Union[bool, Callable],
        # 'create_new': Tuple[str, np.ndarray],
    },
    'name': {
        # 'normalize': 'range',
        'drop_duplicates': False,
        'remove': 'Almond Delight',
        'convert_numeric': 'one_hot_encode',
        # 'missing_value': Any,
        # 'handle_missing': Union[bool, 'remove', 'mean', 'median', 'mode', Any],
        # 'bin': Union[bool, Tuple['frequency', int], Tuple['width', int], Iterable],
        # 'map': Union[bool, Dict],
        # 'remove': True,
        # 'apply': Union[bool, Callable],
        # 'create_new': Tuple[str, np.ndarray],
    },
    'fat': {'drop': True}
}
''
config = {
        # Do these to all the columns, or a specified column
        'all': {
            # Drop the column
            # 'drop': True,
            # Drop duplicate samples
            # 'drop_duplicates': True,
            # If provided, maps feature values to a dictionary
            # 'replace': {
            #     0: 9999,
            #     'K': 'NOT K',
            #     8: 1000
            # },
            # If provided, applies a function to the column
            # 'apply': lambda a: 'HERE' if a == 'K' else a,
            # If provided, specifies a value that is equivalent to the feature being missing
            # 'missing_value': 3,
            # If provided, specifies a method by which to transform samples with missing features
            # 'handle_missing': Union[bool, 'remove', 'mean', 'median', 'mode', Any],
            # 'handle_missing': 'balanced_random',

            # If provided, specifies a method by which to bin the quantative value, or specify custom ranges
            # 'bin': Union[bool, Tuple['frequency', int], Tuple['width', int], Iterable],
            # 'bin': (0, 50, 80, 200),
            # If provided, removes all samples with the given value
            # 'remove': 'K',
            # A ndarray of shape (1, n) of bools to apply to the column to create a new column with the given name
            'add_column': ('yo mamas potass', data['potass'][data['potass'] > 200]),
            # If provided, specifies a method by which to normalize the quantative values
            # 'normalize': Union[bool, 'min-max', 'range'],
            # 'normalize': True,
            # If provided, specifies a method by which to convert a catagorical feature to a quantative one
            # 'convert_numeric': Union[bool, 'assign', 'one_hot_encode'],
            # 'convert_numeric': 'one_hot_encode',
    },
        'mfr': {
            # Drop the column
            # 'drop': False,
            # Drop duplicate samples
            # 'drop_duplicates': False,
            # If provided, maps feature values to a dictionary
            # 'replace': False,
            # If provided, applies a function to the column
            # 'apply': False,
            # If provided, specifies a value that is equivalent to the feature being missing
            # 'missing_value': 'K',
            # If provided, specifies a method by which to transform samples with missing features
            # 'handle_missing': Union[bool, 'remove', 'mean', 'median', 'mode', Any],
            # 'handle_missing': data.type,
            # If provided, specifies a method by which to bin the quantative value, or specify custom ranges
            # 'bin': Union[bool, Tuple['frequency', int], Tuple['width', int], Iterable],
            # 'bin': (0, 50, 80, 200),
            # If provided, removes all samples with the given value
            # 'remove': 'K',
            # A ndarray of shape (1, n) of bools to apply to the column to create a new column with the given name
            # 'add_column': ('yo mamas potass', data['potass'][data['potass'] > 200]),
            # If provided, specifies a method by which to normalize the quantative values
            # 'normalize': Union[bool, 'min-max', 'range'],
            # 'normalize': True,
            # If provided, specifies a method by which to convert a catagorical feature to a quantative one
            # 'convert_numeric': Union[bool, 'assign', 'one_hot_encode'],
            # 'convert_numeric': False,
            # 'queries': False
        },
    'fiber':{
        'queries': ('calories > 100', data.protein),
    },
    'name':{'convert_numeric':'assign'}
}

# unclean = insertSample(data, data.iloc[1], index=0)
unclean = data.copy()
display(unclean.head())
clean(unclean, config, verbose=True).head()




%autoreload 2

# data.name._get_numeric_data()
_catagoricalTypes = ['bool', 'bool_', 'object', 'object_', 'Interval', 'bool8', 'category']
_quantitativeTypes = ['number']
_timeTypes = ['datetimetz', 'timedelta', 'datetime']
# data.select_dtypes(include=_quantitativeTypes)
# data.select_dtypes(include=_catagoricalTypes)
# data.select_dtypes(include=_timeTypes)
assert np.all(data.select_dtypes(include=_catagoricalTypes) == data.select_dtypes(exclude=_quantitativeTypes))
assert np.all(data.select_dtypes(exclude=_catagoricalTypes) == data.select_dtypes(include=_quantitativeTypes))
# data.cups.dtype
# data.cups in
# quantataetive(data.cups)
data.cups.name in catagorical(pd.DataFrame(data.cups))




targets_file = "https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/biking_holdout_test_mini_answers.csv"
targets = pd.read_csv(targets_file)
targets['actual'] = targets.casual + targets.registered
targets.drop(columns=['casual','registered'],inplace=True)

targets



pred = pd.read_csv('/home/leonard/Downloads/holdoutPredictions (12).csv')
pred





from data import *
%autoreload 2
from data import *
# mean_squared_error(targets, pred)

# evaluateQ(targets.iloc[:,0], pred.iloc[:,0], line=True)
sns.scatterplot(targets-pred)
# display(type(targets))
# pred
# type(targets)
# pd.Series(targets.iloc[:,0])
# (targets.astype(np.float64), pred)
'''
