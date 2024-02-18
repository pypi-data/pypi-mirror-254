import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple
from sklearn.metrics import roc_curve, auc
from utils_tdinoto.utils_io import create_dir_if_not_exist
import os
from matplotlib.ticker import MaxNLocator
from utils_tdinoto.utils_lists import first_argmin, first_argmax
import torch


def plot_roc_curve(flat_y_test: list,
                   flat_y_pred_proba: list,
                   nb_classes: int,
                   cv_folds: int,
                   out_path: str,
                   legend_label: str,
                   plot: bool = True,
                   save: bool = True) -> Tuple[np.ndarray, np.ndarray, float]:
    """This function computes FPR, TPR and AUC. Then, it plots the ROC curve.
    For the multi-class scenario, it computes the micro-average ROC curve and ROC area.
    Args:
        flat_y_test: labels
        flat_y_pred_proba: predictions
        nb_classes: number of classes
        cv_folds: number of folds in the cross-validation
        out_path: path where we save the figure
        legend_label: label to use in the legend
        plot: if True, the ROC curve will be displayed
        save: if True, save the figure to disk
    Returns:
        fpr: false positive rates
        tpr: true positive rates
        auc_roc: area under the ROC curve
    """
    if nb_classes == 2:  # binary classification

        # for every prediction, extract probabilistic output for the positive class
        # TODO: TO BE TESTED!!! I adapted it from the glioma code, but I'm not sure it works
        flat_y_pred_proba = [pred[1] for pred in flat_y_pred_proba]  # type: list

        fpr, tpr, _ = roc_curve(flat_y_test, flat_y_pred_proba, pos_label=1)
        tpr[0] = 0.0  # ensure that first element is 0
        tpr[-1] = 1.0  # ensure that last element is 1
        auc_roc = auc(fpr, tpr)
        if plot:
            fig, ax = plt.subplots()
            ax.plot(fpr, tpr, color="b", label=f'{legend_label} (AUC = {auc_roc:.2f})', lw=2, alpha=.8)
            ax.set(xlim=[-0.05, 1.05], ylim=[-0.05, 1.05])
            ax.set_title(f"ROC curve; {cv_folds}-fold CV", weight="bold", fontsize=15)
            ax.set_xlabel('FPR (1- specificity)', fontsize=12)
            ax.set_ylabel('TPR (sensitivity)', fontsize=12)
            ax.legend(loc="lower right")
            if save:
                fig.savefig(out_path)  # save the full figure

        return fpr, tpr, auc_roc

    # if instead there are more than 2 classes, we need to compute the ROC curve for each class;
    # we use the one-vs-all (also called one-vs-rest) approach, where we compute the ROC curve for each class against all the other classes
    else:
        # convert the predictions to a numpy array
        y_pred_probab_np = np.asanyarray(flat_y_pred_proba)  # type: np.ndarray

        # transform the labels into 1-hot encoding format
        y_test_one_hot = torch.nn.functional.one_hot(torch.as_tensor(flat_y_test),
                                                     num_classes=nb_classes).detach().cpu().numpy()  # type: np.ndarray

        # store the fpr, tpr, and roc_auc for all averaging strategies
        fpr, tpr, auc_roc = dict(), dict(), dict()
        # Compute micro-average ROC curve and ROC area
        fpr["micro"], tpr["micro"], _ = roc_curve(y_test_one_hot.ravel(), y_pred_probab_np.ravel())
        auc_roc["micro"] = auc(fpr["micro"], tpr["micro"])

        # TODO: consider adding also macro-average (see scikit-learn tutorial)

        return fpr["micro"], tpr["micro"], auc_roc["micro"]


def save_loss_curves(train_loss: list,
                     val_loss: list,
                     image_dir: str,
                     image_filename: str) -> None:
    """ This function plots the training loss curve. If val_loss is not empty, it also plots the validation loss curve
    (overlayed) with a dashed line and highlights the minimum value with a red circle.
    Args:
        train_loss: training loss
        val_loss: validation loss
        image_dir: path where we want to save the image
        image_filename: name of image
    """
    create_dir_if_not_exist(image_dir)  # if output dir does not exist, create it

    x_axis = np.arange(1, len(train_loss) + 1, 1)  # since the input vectors have same length, just use one of them to extract epochs

    fig, ax1 = plt.subplots()  # create figure
    color_1 = 'tab:red'
    ax1.plot(x_axis, train_loss, color=color_1, label='Train loss')

    if val_loss:  # if val_loss is not empty
        assert len(train_loss) == len(val_loss), "We expect to have the same length for train_loss and val_loss"
        ax1.plot(x_axis, val_loss, "--", color=color_1, label='Val loss')
        idx_min = first_argmin(val_loss)  # find index of minimum value
        ax1.plot(x_axis[idx_min], min(val_loss), 'ro', markersize="10", label='min val_loss = {:.4f}'.format(min(val_loss)))  # highlight maximum value in the plot

    ax1.tick_params(axis='y', labelcolor=color_1)
    ax1.set_xlabel('Epochs')
    ax1.set_ylabel("Loss")
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))  # only keep integers in x axis for epochs
    ax1.set_ylim([0, 1.3])

    fig.suptitle('Loss Curves', fontsize=16, fontweight='bold')
    fig.legend(loc="upper right")
    image_path = os.path.join(image_dir, image_filename)
    fig.savefig(image_path)  # save the full figure


def save_validation_metrics(val_accuracy: list,
                            val_weighted_f1: list,
                            image_dir: str,
                            image_filename: str) -> None:
    """This function plots the train/val metrics
    Args:
        val_accuracy: validation accuracy
        val_weighted_f1: validation weighted f1 score
        image_dir: path where we want to save the image
        image_filename: image filename
    """
    create_dir_if_not_exist(image_dir)  # if output dir does not exist, create it
    assert len(val_accuracy) == len(val_weighted_f1), "We expect to have the same length for val_accuracy and val_weighted_f1"

    x_axis = np.arange(1, len(val_accuracy) + 1, 1)  # since the two input vectors have same length, just use one of the two to extract epochs
    fig2, ax1 = plt.subplots()  # create figure
    color_1 = 'tab:green'
    color_2 = 'tab:blue'
    ax1.plot(x_axis, val_accuracy, "--", color=color_1, label='Val accuracy')
    ax1.plot(x_axis, val_weighted_f1, "--", color=color_2, label='Val weighted f1-score')
    idx_max = first_argmax(val_weighted_f1)  # find index of maximum value
    ax1.plot(x_axis[idx_max], max(val_weighted_f1), 'ro', markersize="10", label='max val_f1 = {:.4f}'.format(max(val_weighted_f1)))  # highlight maximum value in the plot
    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Validation metrics')
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))  # only keep integers in x axis

    fig2.suptitle('Val Curves', fontsize=16, fontweight='bold'), fig2.legend(loc="upper right")
    image_path = os.path.join(image_dir, image_filename)
    fig2.savefig(image_path)  # save the full figure
