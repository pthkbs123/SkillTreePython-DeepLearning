import matplotlib.pyplot as plt



def plot_lcurve(hists, titles, colors):
  plt.figure(figsize = (12,4))
  # loss
  plt.subplot(121)
  for i,hist in enumerate(hists):
    
    loss = hist.history['loss']
    val_loss = hist.history['val_loss']
    epochs = range(1, 1+len(loss))
    plt.plot(epochs, loss, linestyle = ':', label = f'{titles[i]} train loss', c = colors[i])
    plt.plot(epochs, val_loss, marker = '.', label = f'{titles[i]} val_loss', c = colors[i])
    plt.legend();plt.grid(True);plt.xticks(epochs)
    plt.xlabel('Epochs');plt.ylabel('Loss')

    x, y = epochs[-1], hist.history['loss'][-1]
    plt.text(x, y, np.round(y,2), c = colors[i])
    x, y = epochs[-1], hist.history['val_loss'][-1]
    plt.text(x, y, np.round(y,2), c = colors[i])
  # acc
  plt.subplot(122)
  for i,hist in enumerate(hists):
    acc = hist.history['acc']
    val_acc = hist.history['val_acc']
    
    epochs = range(1, 1+len(loss))
    plt.plot(epochs, acc, linestyle = ':', label = f'{titles[i]} train acc', c = colors[i])
    plt.plot(epochs, val_acc, marker = '.', label = f'{titles[i]} val_acc', c = colors[i])
    plt.legend();plt.grid(True);plt.xticks(epochs)
    plt.xlabel('Epochs');plt.ylabel('Acc')

    x, y = epochs[-1], hist.history['acc'][-1]
    plt.text(x, y, np.round(y,2), c = colors[i])
    x, y = epochs[-1], hist.history['val_acc'][-1]
    plt.text(x, y, np.round(y,2), c = colors[i])

  plt.show()