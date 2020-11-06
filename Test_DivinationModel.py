import unittest
import io
import sys
from DivinationModel import DivinationModel

class Test_DivinationModel(unittest.TestCase):

    #DM-P DM-PPC
    def test_DivinationModelPull(self):
        divModel = DivinationModel()
        divModel.pullDivination()
        assert divModel.divinationStats["House of Mirrors"] is not None
    
    #DM-PPC
    def test_PricePerStack(self):
        divModel = DivinationModel()
        divModel.pullDivination()
        divModel.calculatePricePerStack()
        assert divModel.divinationStats["House of Mirrors"]['StackPrice'] is not None

    def test_ROI(self):
        divModel = DivinationModel()
        divModel.pullDivination()
        divModel.calculateROI()
        assert divModel.divinationStats["House of Mirrors"]['ROI'] is not None

    def test_Main(self):
        divModel = DivinationModel()
        divModel.main()
        
        assert divModel.getDivModel() is not None

if __name__ == "__main__":
    unittest.main()