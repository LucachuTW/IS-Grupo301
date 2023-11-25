import unittest
import houseEnv
import houseModel


class testing(unittest.TestCase):
    def test_createsController(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        self.assertIsInstance(control, houseEnv.HouseEnv)
        # Check that houseEnv is instantiated

    def test_addDrugs1(self):
        # @SantiagoRR2004
        # Modified by @antonoterof
        tester = "cabinet"
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus(tester, False)
        maximun = control.getModel().getCapacity(tester)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.checkAddDrug("cabinet", maximun - initialValue), False)
        self.assertEqual(control.getModel().getDrug(tester), initialValue)
        # Fails because it isn't open

    def test_addDrugs2(self):
        # @SantiagoRR2004
        # Modified by @antonoterof
        tester = "cabinet"
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus(tester, True)
        maximun = control.getModel().getCapacity(tester)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.checkAddDrug(tester, maximun - initialValue), True)
        self.assertEqual(control.getModel().getDrug(tester), initialValue)
        # The tester can be filled

    def test_addDrugs3(self):
        # @SantiagoRR2004
        # Modified by @antonoterof
        tester = "cabinet"
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus(tester, True)
        maximun = control.getModel().getCapacity(tester)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(
            control.checkAddDrug(tester, maximun - initialValue + 1), False
        )
        self.assertEqual(control.getModel().getDrug(tester), initialValue)
        # Overfills the tester

    def test_addDrugs4(self):
        # @SantiagoRR2004
        # Modified by @antonoterof
        tester = "cabinet"
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus(tester, True)
        maximun = control.getModel().getCapacity(tester)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.checkAddDrug(tester, -maximun - 1), False)
        self.assertEqual(control.getModel().getDrug(tester), initialValue)
        # Tries to remove too many from tester

    def test_addDrugs5(self):
        # @SantiagoRR2004
        # Modified by @antonoterof
        tester = "robot"
        control = houseModel.HouseModel().getController()
        maximun = control.getModel().getCapacity(tester)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.checkAddDrug(tester, maximun - initialValue), True)
        self.assertEqual(control.getModel().getDrug(tester), initialValue)
        # Could fill up the tester that doesn't have attribute open without problems

    def test_addDrugs6(self):
        # @SantiagoRR2004
        # Modified by @antonoterof
        tester = "cabinet"
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus(tester, True)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.checkAddDrug(tester, -initialValue), True)
        self.assertEqual(control.getModel().getDrug(tester), initialValue)
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
        # Check that the agents are nearby

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
        # Check that the agents are nearby

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
        # Check that the agents are nearby

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
        # Check that the agents are nearby

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
        # Check that the agents are nearby

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
        # Check that the agents are nearby

    def test_transferDrugs1(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        giver = "cabinet"
        reciever = "robot"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict(giver, "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict(reciever, "symbol")
        )
        control.getModel().setOpenStatus(giver, True)

        initialValue1 = control.getModel().getDrug(giver)
        maximun1 = control.getModel().getCapacity(giver)
        initialValue2 = control.getModel().getDrug(reciever)
        maximun2 = control.getModel().getCapacity(reciever)

        control.getModel().addDrug(giver, maximun1 - initialValue1)
        control.getModel().addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), True)
        self.assertEqual(control.getModel().getDrug(giver), maximun1 - 1)
        self.assertEqual(control.getModel().getDrug(reciever), 1)
        # No failures, it transfers 1 Drug

    def test_transferDrugs2(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        giver = "robot"
        reciever = "cabinet"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict(giver, "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict(reciever, "symbol")
        )
        control.getModel().setOpenStatus(reciever, True)

        initialValue1 = control.getModel().getDrug(giver)
        maximun1 = control.getModel().getCapacity(giver)
        initialValue2 = control.getModel().getDrug(reciever)
        maximun2 = control.getModel().getCapacity(reciever)

        control.getModel().addDrug(giver, maximun1 - initialValue1)
        control.getModel().addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), True)
        self.assertEqual(control.getModel().getDrug(giver), maximun1 - 1)
        self.assertEqual(control.getModel().getDrug(reciever), 1)
        # No failures, it transfers 1 Drug

    def test_transferDrugs3(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "cabinet"
        giver = "robot"
        reciever = "cabinet"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict(giver, "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict(reciever, "symbol")
        )
        control.getModel().setOpenStatus(reciever, True)

        initialValue1 = control.getModel().getDrug(giver)
        maximun1 = control.getModel().getCapacity(giver)
        initialValue2 = control.getModel().getDrug(reciever)
        maximun2 = control.getModel().getCapacity(reciever)

        control.getModel().addDrug(giver, maximun1 - initialValue1)
        control.getModel().addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), False)
        self.assertEqual(control.getModel().getDrug(giver), maximun1)
        self.assertEqual(control.getModel().getDrug(reciever), 0)
        # Fails because mover can't transfer because it can't move on it's own

    def test_transferDrugs4(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        giver = "robot"
        reciever = "cabinet"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict(giver, "symbol")
        )
        model.setPosition(
            1, 1, control.getModel().getAttributeFromDict(reciever, "symbol")
        )
        control.getModel().setOpenStatus(reciever, True)

        initialValue1 = control.getModel().getDrug(giver)
        maximun1 = control.getModel().getCapacity(giver)
        initialValue2 = control.getModel().getDrug(reciever)
        maximun2 = control.getModel().getCapacity(reciever)

        control.getModel().addDrug(giver, maximun1 - initialValue1)
        control.getModel().addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), False)
        self.assertEqual(control.getModel().getDrug(giver), maximun1)
        self.assertEqual(control.getModel().getDrug(reciever), 0)
        # Fails because they aren't adjacent

    def test_transferDrugs5(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        giver = "cabinet"
        reciever = "robot"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict(giver, "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict(reciever, "symbol")
        )
        control.getModel().setOpenStatus(giver, True)

        initialValue1 = control.getModel().getDrug(giver)
        maximun1 = control.getModel().getCapacity(giver)
        initialValue2 = control.getModel().getDrug(reciever)
        maximun2 = control.getModel().getCapacity(reciever)

        control.getModel().addDrug(giver, maximun1 - initialValue1)
        control.getModel().addDrug(reciever, -initialValue2)

        self.assertEqual(
            control.transferDrugs(mover, giver, reciever, maximun2 + 1), False
        )
        self.assertEqual(control.getModel().getDrug(giver), maximun1)
        self.assertEqual(control.getModel().getDrug(reciever), 0)
        # Not enough space on the reciever

    def test_transferDrugs6(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        giver = "robot"
        reciever = "cabinet"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict(giver, "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict(reciever, "symbol")
        )
        control.getModel().setOpenStatus(reciever, True)

        initialValue1 = control.getModel().getDrug(giver)
        maximun1 = control.getModel().getCapacity(giver)
        initialValue2 = control.getModel().getDrug(reciever)
        maximun2 = control.getModel().getCapacity(reciever)

        control.getModel().addDrug(giver, maximun1 - initialValue1)
        control.getModel().addDrug(reciever, -initialValue2)

        self.assertEqual(
            control.transferDrugs(mover, giver, reciever, maximun1 + 1), False
        )
        self.assertEqual(control.getModel().getDrug(giver), maximun1)
        self.assertEqual(control.getModel().getDrug(reciever), 0)
        # Not enough drugs on the giver

    def test_transferDrugs7(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        giver = "cabinet"
        reciever = "robot"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict(giver, "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict(reciever, "symbol")
        )
        control.getModel().setOpenStatus(giver, False)

        initialValue1 = control.getModel().getDrug(giver)
        maximun1 = control.getModel().getCapacity(giver)
        initialValue2 = control.getModel().getDrug(reciever)
        maximun2 = control.getModel().getCapacity(reciever)

        control.getModel().addDrug(giver, maximun1 - initialValue1)
        control.getModel().addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), False)
        self.assertEqual(control.getModel().getDrug(giver), maximun1)
        self.assertEqual(control.getModel().getDrug(reciever), 0)
        # Cabinet isn't open

    def test_checkOpeneable1(self):
        # @Ventupentu
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        self.assertIsInstance(control.checkOpeneable("doors"), bool)

    def test_checkOpeneable2(self):
        # @Ventupentu
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        element = "cabinet"
        open = control.getModel().getAttributeFromDict(element, "openable")
        self.assertEqual(control.checkOpeneable(element), open)

    def test_checkIfShareable1(self):
        # @SantiagoRR2004
        # No problems
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        element = "cabinet"

        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", True)
        model.setAttributeFromDict(element, "open", True)

        self.assertEqual(control.checkIfShareable(element), True)

    def test_checkIfShareable2(self):
        # @SantiagoRR2004
        # It isn't open
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        element = "cabinet"

        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", True)
        model.setAttributeFromDict(element, "open", False)

        self.assertEqual(control.checkIfShareable(element), False)

    def test_checkIfShareable3(self):
        # @SantiagoRR2004
        # No problems
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        element = "cabinet"

        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", False)

        booleans = [True, False]
        for dontCareIfOpen in booleans:
            model.setAttributeFromDict(element, "open", dontCareIfOpen)
            self.assertEqual(control.checkIfShareable(element), True)

    def test_checkIfShareable4(self):
        # @SantiagoRR2004
        # Object can't share the space
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        element = "cabinet"

        model.setAttributeFromDict(element, "semisolid", False)

        booleans = [True, False]
        for dontCareIfOpenable in booleans:
            model.setAttributeFromDict(element, "openable", dontCareIfOpenable)
            for dontCareIfOpen in booleans:
                model.setAttributeFromDict(element, "open", dontCareIfOpen)
                self.assertEqual(control.checkIfShareable(element), False)

    def test_checkIfMovableTo1(self):
        # @SantiagoRR2004
        # No problems
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.setPosition(0, 0, 0)
        self.assertEqual(control.checkIfMovableTo(0, 0), True)

    def test_checkIfMovableTo2(self):
        # @SantiagoRR2004
        # Number is prime
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.setPosition(0, 0, 6)
        self.assertEqual(control.checkIfMovableTo(0, 0), False)

    def test_checkIfMovableTo3(self):
        # @SantiagoRR2004
        # No problems
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.removeValue(element)
        model.setPosition(0, 0, elementSymbol)

        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", True)
        model.setAttributeFromDict(element, "open", True)

        self.assertEqual(control.checkIfMovableTo(0, 0, element), True)

    def test_checkIfMovableTo4(self):
        # @SantiagoRR2004
        # No problems
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.removeValue(element)
        model.setPosition(0, 0, elementSymbol)

        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", False)

        booleans = [True, False]
        for dontCareIfOpen in booleans:
            model.setAttributeFromDict(element, "open", dontCareIfOpen)
            self.assertEqual(control.checkIfMovableTo(0, 0, element), True)

    def test_checkIfMovableTo5(self):
        # @SantiagoRR2004
        # Object isn't semisolid
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.removeValue(element)
        model.setPosition(0, 0, elementSymbol)

        model.setAttributeFromDict(element, "semisolid", False)

        booleans = [True, False]
        for dontCareIfOpenable in booleans:
            model.setAttributeFromDict(element, "openable", dontCareIfOpenable)
            for dontCareIfOpen in booleans:
                model.setAttributeFromDict(element, "open", dontCareIfOpen)
                self.assertEqual(control.checkIfMovableTo(0, 0, element), False)

    def test_checkIfMovableTo6(self):
        # @SantiagoRR2004
        # Object isn't open
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.removeValue(element)
        model.setPosition(0, 0, elementSymbol)

        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", True)
        model.setAttributeFromDict(element, "open", False)

        self.assertEqual(control.checkIfMovableTo(0, 0, element), False)

    def test_moveTo1(self):
        # @SantiagoRR2004
        # No problem
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(0, 0, moverSymbol)
        model.setPosition(1, 0, 0)

        self.assertEqual(control.moveTo(mover, moved, 1, 0), True)
        self.assertEqual(model.getPosition(0, 0), 0)
        self.assertEqual(model.getPosition(1, 0), moverSymbol)

    def test_moveTo2(self):
        # @SantiagoRR2004
        # No problem
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(0, 0, moverSymbol)
        model.setPosition(0, 1, 0)

        self.assertEqual(control.moveTo(mover, moved, 0, 1), True)
        self.assertEqual(model.getPosition(0, 0), 0)
        self.assertEqual(model.getPosition(0, 1), moverSymbol)

    def test_moveTo3(self):
        # @SantiagoRR2004
        # No problem
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(1, 0, moverSymbol)
        model.setPosition(0, 0, 0)

        self.assertEqual(control.moveTo(mover, moved, 0, 0), True)
        self.assertEqual(model.getPosition(1, 0), 0)
        self.assertEqual(model.getPosition(0, 0), moverSymbol)

    def test_moveTo4(self):
        # @SantiagoRR2004
        # No problem
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(0, 1, moverSymbol)
        model.setPosition(0, 0, 0)

        self.assertEqual(control.moveTo(mover, moved, 0, 0), True)
        self.assertEqual(model.getPosition(0, 1), 0)
        self.assertEqual(model.getPosition(0, 0), moverSymbol)

    def test_moveTo5(self):
        # @SantiagoRR2004
        # Can't move diagonally
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(0, 0, moverSymbol)
        model.setPosition(1, 1, 0)

        self.assertEqual(control.moveTo(mover, moved, 1, 1), False)
        self.assertEqual(model.getPosition(0, 0), moverSymbol)
        self.assertEqual(model.getPosition(1, 1), 0)

    def test_moveTo6(self):
        # @SantiagoRR2004
        # Can't move too far away
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(0, 0, moverSymbol)
        model.setPosition(2, 2, 0)

        self.assertEqual(control.moveTo(mover, moved, 2, 2), False)
        self.assertEqual(model.getPosition(0, 0), moverSymbol)
        self.assertEqual(model.getPosition(2, 2), 0)

    def test_moveTo7(self):
        # @SantiagoRR2004
        # Object can't move itself
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = False
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(0, 0, moverSymbol)
        model.setPosition(1, 0, 0)

        self.assertEqual(control.moveTo(mover, moved, 1, 0), False)
        self.assertEqual(model.getPosition(0, 0), moverSymbol)
        self.assertEqual(model.getPosition(1, 0), 0)

    def test_moveTo8(self):
        # @SantiagoRR2004
        # Can't move to occupied by 2 others
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(0, 0, moverSymbol)
        model.setPosition(1, 0, 6)

        self.assertEqual(control.moveTo(mover, moved, 1, 0), False)
        self.assertEqual(model.getPosition(0, 0), moverSymbol)
        self.assertEqual(model.getPosition(1, 0), 0)

    def test_moveTo9(self):
        # @SantiagoRR2004
        # No problems
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["mover"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = "cabinet"
        model.getAttributeFromDict(moved, "moving")["auto"] = False
        model.getAttributeFromDict(moved, "moving")["moved"] = True
        movedSymbol = model.getAttributeFromDict(mover, "symbol")

        model.removeValue(mover)
        model.removeValue(moved)

        model.setPosition(0, 0, movedSymbol)
        model.setPosition(0, 1, moverSymbol)
        model.setPosition(1, 0, 0)

        self.assertEqual(control.moveTo(mover, moved, 1, 0), True)
        self.assertEqual(model.getPosition(0, 0), 0)
        self.assertEqual(model.getPosition(1, 0), movedSymbol)
        self.assertEqual(model.getPosition(0, 1), moverSymbol)

    def test_moveTo10(self):
        # @SantiagoRR2004
        # No problem
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moved = mover
        model.setAttributeFromDict(moved, "semisolid", True)
        model.setAttributeFromDict(moved, "openable", True)
        model.setAttributeFromDict(moved, "open", True)
        movedSymbol = model.getAttributeFromDict(moved, "symbol")
        model.removeValue(mover)

        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.remove(element)
        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", True)
        model.setAttributeFromDict(element, "open", True)

        model.setPosition(0, 0, movedSymbol)
        model.setPosition(1, 0, elementSymbol)

        self.assertEqual(control.moveTo(mover, moved, 1, 0), True)
        self.assertEqual(model.getPosition(0, 0), 0)
        self.assertEqual(model.getPosition(1, 0), movedSymbol * elementSymbol)

    def test_moveTo11(self):
        # @SantiagoRR2004
        # Other item isn't open so it doesn't work
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moved = mover
        model.setAttributeFromDict(moved, "semisolid", True)
        model.setAttributeFromDict(moved, "openable", False)
        movedSymbol = model.getAttributeFromDict(moved, "symbol")
        model.removeValue(mover)

        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.remove(element)
        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", True)
        model.setAttributeFromDict(element, "open", False)

        model.setPosition(0, 0, movedSymbol)
        model.setPosition(1, 0, elementSymbol)

        booleans = [True, False]
        for dontCareIfOpen in booleans:
            model.setAttributeFromDict(moved, "open", dontCareIfOpen)
            self.assertEqual(control.moveTo(mover, moved, 1, 0), False)
            self.assertEqual(model.getPosition(0, 0), movedSymbol)
            self.assertEqual(model.getPosition(1, 0), elementSymbol)

    def test_moveTo12(self):
        # @SantiagoRR2004
        # Other item can't share space with each other
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moved = mover
        movedSymbol = model.getAttributeFromDict(moved, "symbol")
        model.removeValue(mover)

        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.remove(element)
        model.setAttributeFromDict(element, "semisolid", False)

        model.setPosition(0, 0, movedSymbol)
        model.setPosition(1, 0, elementSymbol)

        booleans = [True, False]
        for dontCareIfSemisolidOfMoved in booleans:
            model.setAttributeFromDict(moved, "semisolid", dontCareIfSemisolidOfMoved)
            for dontCareIfOpenableOfMoved in booleans:
                model.setAttributeFromDict(moved, "openable", dontCareIfOpenableOfMoved)
                for dontCareIfOpenOfMoved in booleans:
                    model.setAttributeFromDict(moved, "open", dontCareIfOpenOfMoved)
                    for dontCareIfOpenableOfElement in booleans:
                        model.setAttributeFromDict(
                            element, "openable", dontCareIfOpenableOfElement
                        )
                        for dontCareIfOpenOfElement in booleans:
                            model.setAttributeFromDict(
                                element, "open", dontCareIfOpenOfElement
                            )
                            self.assertEqual(control.moveTo(mover, moved, 1, 0), False)
                            self.assertEqual(model.getPosition(0, 0), movedSymbol)
                            self.assertEqual(model.getPosition(1, 0), elementSymbol)
