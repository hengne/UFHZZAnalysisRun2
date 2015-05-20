import FWCore.ParameterSet.Config as cms

process = cms.Process("UFHZZ4LAnalysis")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.categories.append('UFHZZ4LAna')

process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.GlobalTag.globaltag='START53_V23::All'

process.Timing = cms.Service("Timing",
                             summaryOnly = cms.untracked.bool(True)
                             )


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

myfilelist = cms.untracked.vstring()
myfilelist.extend( [

        # the sync file
        #'file:/cms/data/store/mc/Phys14DR/GluGluToHToZZTo4L_M-125_13TeV-powheg-pythia6/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/3295EF7C-2070-E411-89C4-7845C4FC35DB.root'
        #'root://cmsxrootd.fnal.gov//store/mc/Phys14DR/GluGluToHToZZTo4L_M-125_13TeV-powheg-pythia6/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/3295EF7C-2070-E411-89C4-7845C4FC35DB.root'
        
        # all files
        #'/store/mc/Phys14DR/GluGluToHToZZTo4L_M-125_13TeV-powheg-pythia6/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/148E558C-946F-E411-AFA7-7845C4FC3A52.root',
        #'/store/mc/Phys14DR/GluGluToHToZZTo4L_M-125_13TeV-powheg-pythia6/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/3295EF7C-2070-E411-89C4-7845C4FC35DB.root',
        #'/store/mc/Phys14DR/GluGluToHToZZTo4L_M-125_13TeV-powheg-pythia6/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/40729A64-946F-E411-B6CE-7845C4FC3A52.root',
        #'/store/mc/Phys14DR/GluGluToHToZZTo4L_M-125_13TeV-powheg-pythia6/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/60908275-2070-E411-94E2-7845C4FC3A58.root',
        #'/store/mc/Phys14DR/GluGluToHToZZTo4L_M-125_13TeV-powheg-pythia6/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/84965C0D-946F-E411-99FA-848F69FD2955.root',
        #'/store/mc/Phys14DR/GluGluToHToZZTo4L_M-125_13TeV-powheg-pythia6/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/10000/A2ABB939-3670-E411-BCA8-848F69FD4553.root',
        #'/store/mc/Phys14DR/GluGluToHToZZTo4L_M-125_13TeV-powheg-pythia6/MINIAODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/10000/C0E81726-3670-E411-BE66-008CFA007CE0.root'

        # Categories sync
#        'file:/scratch/osghpc/dsperka/Run2/HZZ4l/CMSSW_7_2_0/src/ggH_JHU_125.MINIAODSIM00.root',
#        'file:/scratch/osghpc/dsperka/Run2/HZZ4l/CMSSW_7_2_0/src/VBF_JHU_125.MINIAODSIM00.root',
#        'file:/scratch/osghpc/dsperka/Run2/HZZ4l/CMSSW_7_2_0/src/WminusH_JHU_125.MINIAODSIM00.root',
#        'file:/scratch/osghpc/dsperka/Run2/HZZ4l/CMSSW_7_2_0/src/ZH_JHU_125.MINIAODSIM00.root',
#        'file:/scratch/osghpc/dsperka/Run2/HZZ4l/CMSSW_7_2_0/src/ttH_JHU_125.MINIAODSIM00.root',
     '/store/cmst3/group/susy/gpetrucc/13TeV/Phys14DR/MINIAODSIM/ggH_JHU_125/ggH_JHU_125.MINIAODSIM00.root',
     '/store/cmst3/group/susy/gpetrucc/13TeV/Phys14DR/MINIAODSIM/VBF_JHU_125/VBF_JHU_125.MINIAODSIM00.root',
     '/store/cmst3/group/susy/gpetrucc/13TeV/Phys14DR/MINIAODSIM/WminusH_JHU_125/WminusH_JHU_125.MINIAODSIM00.root',
     '/store/cmst3/group/susy/gpetrucc/13TeV/Phys14DR/MINIAODSIM/ZH_JHU_125/ZH_JHU_125.MINIAODSIM00.root',
     '/store/cmst3/group/susy/gpetrucc/13TeV/Phys14DR/MINIAODSIM/ttH_JHU_125/ttH_JHU_125.MINIAODSIM00.root',

        
]
)

process.source = cms.Source("PoolSource",fileNames = myfilelist,
#                             duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
#                             eventsToProcess = cms.untracked.VEventRange('1:2130-1:2130')#'1:4093-1:4093','1:2755-1:2755','1:2130-1:2130')
			     
                            )

#process.source.eventsToProcess = cms.untracked.VEventRange("1:894701:721")
#process.source.eventsToProcess = cms.untracked.VEventRange("1:894700:1954")
#process.source.eventsToProcess = cms.untracked.VEventRange("1:894701:1983")

process.TFileService = cms.Service("TFileService",
#                                   fileName = cms.string("GluGluToHToZZTo4L_M-125_13TeV-powheg-pythia6_PU20bx25_PAT_testAna.root")
#                                   fileName = cms.string("EventCat.root")
                                   fileName = cms.string("EventCat_test_1.root")
)

'''
process.reCorrectedPatJets = cms.EDProducer("PatJetReCorrector",
                                            jets = cms.InputTag('selectedPatJets'),
                                            payload = cms.string('AK5PF'),
                                            rho = cms.InputTag('kt6PFJets', 'rho','RECO'),
                                            levels = cms.vstring('L1FastJet','L2Relative','L3Absolute')
                                            )
'''

# clean muons by segments 
process.boostedMuons = cms.EDProducer("PATMuonCleanerBySegments",
				     src = cms.InputTag("slimmedMuons"),
				     preselection = cms.string("track.isNonnull"),
				     passthrough = cms.string("isGlobalMuon && numberOfMatches >= 2"),
				     fractionOfSharedSegments = cms.double(0.499),
				     )

# Electron MVA ID producer
process.mvaNonTrigV025nsPHYS14 = cms.EDProducer("SlimmedElectronMvaIDProducer",
                                     electronsCollection = cms.InputTag("slimmedElectrons","","PAT"),
                                     method = cms.string("BDTSimpleCat"),
                                     mvaWeightFile = cms.vstring(
                                                  "EgammaAnalysis/ElectronTools/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml",
                                                  "EgammaAnalysis/ElectronTools/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml",
                                                  "EgammaAnalysis/ElectronTools/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml",
                                                  "EgammaAnalysis/ElectronTools/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml",
                                                  "EgammaAnalysis/ElectronTools/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml",
                                                  "EgammaAnalysis/ElectronTools/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml",
                                     ),
                                     Trig = cms.bool(False),
                                     )
     

process.goodPrimaryVertices = cms.EDFilter("VertexSelector",
    filter = cms.bool(True),
    src = cms.InputTag("offlineSlimmedPrimaryVertices"),
    cut = cms.string('!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2')
)


process.Ana = cms.EDAnalyzer('UFHZZ4LAna',
                              photonSrc    = cms.untracked.InputTag("slimmedPhotons"),
                              electronSrc  = cms.untracked.InputTag("mvaNonTrigV025nsPHYS14","NonTrig"),
                              muonSrc      = cms.untracked.InputTag("boostedMuons"),
                              correctedJetSrc = cms.untracked.InputTag("slimmedJets"),
                              jetSrc       = cms.untracked.InputTag("slimmedJets"),
                              metSrc       = cms.untracked.InputTag("slimmedMETs"),
                              vertexSrc    = cms.untracked.InputTag("goodPrimaryVertices"), #or selectedVertices 
                              isMC         = cms.untracked.bool(True),
                              isSignal     = cms.untracked.bool(True),
                              mH           = cms.untracked.double(125.0),
                              CrossSection = cms.untracked.double(0.00544046 ),
                              FilterEff    = cms.untracked.double(1),
                              weightEvents = cms.untracked.bool(True),
                              elRhoSrc     = cms.untracked.InputTag("fixedGridRhoFastjetAll"),
                              muRhoSrc     = cms.untracked.InputTag("fixedGridRhoFastjetCentralNeutral"),
                              reweightForPU = cms.untracked.bool(True),
                              verbose = cms.untracked.bool(False)              
#                              verbose = cms.untracked.bool(True)              
                             )

process.AnaAfterHlt = cms.EDAnalyzer('UFHZZ4LAna',
                              photonSrc    = cms.untracked.InputTag("slimmedPhotons"),
                              electronSrc  = cms.untracked.InputTag("mvaNonTrigV025nsPHYS14","NonTrig"),
                              muonSrc      = cms.untracked.InputTag("boostedMuons"),
                              correctedJetSrc = cms.untracked.InputTag("slimmedJets"),
                              jetSrc       = cms.untracked.InputTag("slimmedJets"),
                              metSrc       = cms.untracked.InputTag("slimmedMETs"),
                              vertexSrc    = cms.untracked.InputTag("goodPrimaryVertices"), #or selectedVertices 
                              isMC         = cms.untracked.bool(True),
                              isSignal     = cms.untracked.bool(True),
                              mH           = cms.untracked.double(125.0),
                              CrossSection = cms.untracked.double(0.00544046 ),
                              FilterEff    = cms.untracked.double(1),
                              weightEvents = cms.untracked.bool(True),
                              elRhoSrc     = cms.untracked.InputTag("fixedGridRhoFastjetAll"),
                              muRhoSrc     = cms.untracked.InputTag("fixedGridRhoFastjetCentralNeutral"),
                              reweightForPU = cms.untracked.bool(True),
                              verbose = cms.untracked.bool(False)                          
#                              verbose = cms.untracked.bool(True)
                             )


# Trigger
process.hltHighLevel = cms.EDFilter("HLTHighLevel",
                                    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                                    HLTPaths = cms.vstring(
                                         'HLT_Ele17_Ele12_Ele10_CaloId_TrackId_v1',
                                         'HLT_Ele23_Ele12_CaloId_TrackId_Iso_v1',
                                         'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1',
                                         'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1',
                                         'HLT_Mu23_TrkIsoVVL_Ele12_Gsf_CaloId_TrackId_Iso_MediumWP_v1',
                                         'HLT_Mu8_TrkIsoVVL_Ele23_Gsf_CaloId_TrackId_Iso_MediumWP_v1'
                                    ),
                                    # provide list of HLT paths (or patterns) you want
                                    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
                                    andOr = cms.bool(True),              # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true  
                                    throw = cms.bool(False)              # throw exception on unknown path names 
                                    )


process.load('UFHZZAnalysisRun2.FSRPhotons.fsrPhotons_cff')

process.p = cms.Path(#process.reCorrectedPatJets*
                     process.goodPrimaryVertices*
                     process.fsrPhotonSequence*
		     process.boostedMuons*
                     process.mvaNonTrigV025nsPHYS14*
                     process.Ana*
                     process.hltHighLevel*
                     process.AnaAfterHlt
                     )
