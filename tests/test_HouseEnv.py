import unittest
import houseEnv
import houseModel


class testing(unittest.TestCase):
    def test_createsController(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        self.assertIsInstance(control, houseEnv.HouseEnv)

    def test_addDrugs1(self):
        # @SantiagoRR2004
        tester = "cabinet"
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus(tester, False)
        maximun = control.getModel().getCapacity(tester)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.addDrug("cabinet", maximun - initialValue), False)
        self.assertEqual(control.getModel().getDrug(tester), initialValue)
        # Fails because it isn't open

    def test_addDrugs2(self):
        # @SantiagoRR2004
        tester = "cabinet"
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus(tester, True)
        maximun = control.getModel().getCapacity(tester)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.addDrug(tester, maximun - initialValue), True)
        # Fills up the tester without problems

    def test_addDrugs3(self):
        # @SantiagoRR2004
        tester = "cabinet"
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus(tester, True)
        maximun = control.getModel().getCapacity(tester)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.addDrug(tester, maximun - initialValue + 1), False)
        self.assertEqual(control.getModel().getDrug(tester), initialValue)
        # Overfills the tester

    def test_addDrugs4(self):
        # @SantiagoRR2004
        tester = "cabinet"
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus(tester, True)
        maximun = control.getModel().getCapacity(tester)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.addDrug(tester, -maximun - 1), False)
        self.assertEqual(control.getModel().getDrug(tester), initialValue)
        # Tries to remove too many from tester

    def test_addDrugs5(self):
        # @SantiagoRR2004
        tester = "robot"
        control = houseModel.HouseModel().getController()
        maximun = control.getModel().getCapacity(tester)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.addDrug(tester, maximun - initialValue), True)
        # Fills up the tester that doesn't have attribute open without problems

    def test_addDrugs6(self):
        # @SantiagoRR2004
        tester = "cabinet"
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus(tester, True)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.addDrug(tester, -initialValue), True)
        control.getModel().addDrug(tester, -initialValue)
        self.assertEqual(control.getModel().getDrug(tester), 0)
        # Empties up the tester without problems

    def test_nextToEachOther1(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            0, 1, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), True)

    def test_nextToEachOther2(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), True)

    def test_nextToEachOther3(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), True)

    def test_nextToEachOther4(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(
            0, 1, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), True)

    def test_nextToEachOther5(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            1, 1, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), False)

    def test_nextToEachOther6(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            0, 2, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), False)

    def test_transferDrugs1(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        giver = "cabinet"
        reciever = "robot"

        model.removeValue(mover)
        model.removeValue(giver)

        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict(giver, "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict(mover, "symbol")
        )
        control.getModel().setOpenStatus("cabinet", True)

        initialValue1 = control.getModel().getDrug(giver)
        maximun1 = control.getModel().getCapacity(giver)
        initialValue2 = control.getModel().getDrug(reciever)
        maximun2 = control.getModel().getCapacity(reciever)

        control.getModel().addDrug(giver, maximun1 - initialValue1)
        control.getModel().addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), True)
        self.assertEqual(control.getModel().getDrug(giver), maximun1 - 1)
        self.assertEqual(control.getModel().getDrug(giver), 1)
