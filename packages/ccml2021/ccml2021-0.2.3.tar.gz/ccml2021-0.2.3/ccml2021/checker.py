from emoji import emojize
import os


def do_objects_exist(names, notebook_globals):
    print(
        emojize(":warning:")
        + " オブジェクトの存在確認のみ行っています。内容が正しいかどうかは確認していません。 / This only verifies the presence of the expected objects, without ensuring their contents are pertinent."
    )
    for name in names:
        if name in notebook_globals:
            print("  " + emojize(":thumbs_up:") + " variable `{}` exists".format(name))
        else:
            print(
                "  "
                + emojize(":construction:")
                + " variable `{}` not found".format(name)
            )


def do_file_exists(names):
    print(
        emojize(":warning:")
        + " ファイルの存在確認のみ行っています。内容が正しいかどうかは確認していません / This solely confirms the existence of the expected files, without assuring the relevance of their contents."
    )
    for name in names:
        if os.path.exists(name):
            print("  " + emojize(":thumbs_up:") + " file `{}` exists".format(name))
        else:
            print(
                "  " + emojize(":construction:") + " file `{}` not found".format(name)
            )


def basic3_1(notebook_globals):
    do_objects_exist(
        [
            "X_train_scaled",
            "y_train_scaled",
            "X_test_scaled",
            "pls_model",
            "y_test_pred",
            "pls_model_grid",
            "y_test_pred_grid",
            "svr_model_grid",
            "y_test_pred_svr",
            "y_test_pred_rf",
            "y_test_pred_rf500",
        ],
        notebook_globals,
    )
    do_file_exists(["SVR.png", "RF.png"])


def basic3_2(notebook_globals):
    do_objects_exist(
        [
            "X_train",
            "X_test",
            "y_train",
            "y_test",
            "feature_names",
            "X_train_scaled",
            "y_train_scaled",
            "X_test_scaled",
            "models",
            "y_train_preds",
            "y_test_preds",
            "df",
            "importance_PLS",
            "importance_RF",
        ]
    )

    do_file_exists(
        ["PLS.png", "SVR.png", "RF.png", "importance_PLS.png", "importance_RF.png"]
    )


def basic4_1(notebook_globals):
    do_objects_exist(
        [
            "df",
            "X_train",
            "y_train",
            "x1",
            "x2",
            "X1",
            "X2",
            "X_test",
            "model_svm",
            "Y_test_pred_svm",
            "model_rf",
            "y_test_pred_rf",
        ],
        notebook_globals,
    )
    do_file_exists(["SVC.png", "RandomForestClassifier.png"])


def basic4_2(notebook_globals):
    do_objects_exist(
        [
            "iris",
            "X",
            "y",
            "feature_names",
            "target_names",
            "X_train",
            "X_test",
            "y_train",
            "y_test",
            "X_train_scaled",
            "X_test_scaled",
            "model_svm",
            "y_test_pred_svm",
            "matrix_svm",
            "model_rf",
            "y_test_pred_rf",
            "matrix_rf",
        ],
        notebook_globals,
    )
    # do_file_exists()


def app2(notebook_globals):
    do_objects_exist(
        [
            "move_vector_closer_to_largest_distribution",
            "plot_matrix_and_vector",
            "X",
            "p",
            "p0",
            "p1",
            "p2",
            "diff_t1",
            "diff_t2",
            "diff_t3",
            "t",
            "E",
            "myPCA",
            "model",
            "model_sk",
            "plot_class_components",
            "mean_X",
            "pc",
        ],
        notebook_globals,
    )


def app1(notebook_globals):
    do_objects_exist(
        [
            "X",
            "y",
            "df",
            "X_train",
            "X_test",
            "y_train",
            "y_test",
            "X_train_scaled",
            "y_train_scaled",
            "X_test_scaled",
            "df_metrics",
            "importance_PLS",
            "importance_RF",
        ],
        notebook_globals,
    )
    do_file_exists(
        ["PLS.png", "SVR.png", "RF.png", "importance_PLS.png", "importance_RF.png"]
    )
