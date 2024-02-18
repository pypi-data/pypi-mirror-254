from emoji import emojize
import os


def do_variables_exist(names, notebook_globals):
    print(emojize(":warning:") + " 変数の存在確認のみ行っています。内容が正しいかどうかは確認していません / This only verifies the presence of the expected variables, without ensuring their contents are pertinent.")
    for name in names:
        if name in notebook_globals:
            print("  " + emojize(":thumbs_up:") + " variable `{}` exists".format(name))
        else:
            print("  " + emojize(":construction:") + " variable `{}` not found".format(name))

def do_file_exists(names):
    print(emojize(":warning:") + " ファイルの存在確認のみ行っています。内容が正しいかどうかは確認していません / This solely confirms the existence of the expected files, without assuring the relevance of their contents.")
    for name in names:
        if os.path.exists(name):
            print("  " + emojize(":thumbs_up:") + " file `{}` exists".format(name))
        else:
            print("  " + emojize(":construction:") + " file `{}` not found".format(name))

def basic3_1(notebook_globals):
    do_variables_exist(["X_train_scaled", "y_train_scaled", "X_test_scaled", "pls_model", "y_test_pred", "pls_model_grid", "y_test_pred_grid", "svr_model_grid", "y_test_pred_svr", "y_test_pred_rf", "y_test_pred_rf500"], notebook_globals)
    do_file_exists(["SVR.png", "RF.png"])
