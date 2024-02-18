is_brain = False

if is_brain:
    import Brain


def sub_train_state(epoch,sub_epoch,batch,loader):
    if is_brain:
        Brain(epoch,sub_epoch,batch,loader)
    else:
        print("Sub epoch status : " , epoch,sub_epoch,batch,loader)

def sub_train_end(epoch,sub_epoch,mean_loss):
    if is_brain:
        Brain(epoch,sub_epoch,mean_loss)
    else:
        print("Sub epoch end : ",epoch,sub_epoch,mean_loss)

def validate_state(batch,loader):
    if is_brain:
        Brain(batch,loader)
    else:
        print("Validation status : ",batch,loader)


def validate_end(epoch,mean_loss,img_auc,pix_auc):
    if is_brain:
        Brain(epoch,mean_loss,img_auc,pix_auc)
    else:
        print("Validation End : ",epoch,mean_loss,img_auc,pix_auc)

def test_state(batch,loader):
    if is_brain:
        Brain(batch,loader)
    else:
        print("Test status : ",batch,loader)

def test_end(epoch,mean_loss,img_auc,pix_auc):
    if is_brain:
        Brain(epoch,mean_loss,img_auc,pix_auc)
    else:
        print("Test End : ",epoch,mean_loss,img_auc,pix_auc)