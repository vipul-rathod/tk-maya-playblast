from mentalcore import mapi

def _setCameraDefaults(camera = ''):
    """
    Sets the base defaults for the camera
    @param camera: The name of the camera transform node NOT the shape node!
    @type camera: String
    """
    if not camera:
        camera = utils.getShotCamera()

    if camera:
        camera = cmds.ls(camera, long = True)[0] ## Gah sometimes you know they have the same name in the scene...
        camName = camera
        camShape = cmds.listRelatives(camera, shapes = True)[0]
        cmds.camera(camName, e = True,  displayFilmGate  = 0,  displayResolution = 1,  overscan = 1.19)
        cmds.setAttr("%s.displayGateMask" % camShape, 1)
        cmds.setAttr('%s.displayGateMaskOpacity' % camShape, 1)
        cmds.setAttr('%s.displayGateMaskColor' % camShape, 0, 0, 0, type = 'double3' )
        cmds.setAttr("%s.displayResolution" % camShape, 1)
        cmds.setAttr("%s.displaySafeAction" % camShape, 1)
        cmds.setAttr("%s.journalCommand" % camShape, 0)
        cmds.setAttr("%s.nearClipPlane" % camShape, 0.05)
        cmds.setAttr("%s.overscan" % camShape, 1)

def _setRenderGlobals(width = 1280, height = 720, animation = False):
    cmds.currentUnit(time='pal')
    debug(app = None, method = 'utils._setRenderGlobals', message= 'Set currentTime to pal', verbose = False)
    cmds.currentUnit(linear='cm')
    debug(app = None, method = 'utils._setRenderGlobals', message= 'Set units to cm', verbose = False)

    mel.eval('setAttr defaultResolution.width %s' % width)
    debug(app = None, method = 'utils._setRenderGlobals', message= 'Set defaultResolution width: %s' % width, verbose = False)
    mel.eval('setAttr defaultResolution.height %s' % height)
    debug(app = None, method = 'utils._setRenderGlobals', message= 'Set defaultResolution height: %s' % height, verbose = False)
    mel.eval('setAttr defaultResolution.deviceAspectRatio 1.777')
    debug(app = None, method = 'utils._setRenderGlobals', message= 'Set defaultResolution deviceAspectRatio: 1.777', verbose = False)
    mel.eval('setAttr defaultResolution.pixelAspect 1')
    debug(app = None, method = 'utils._setRenderGlobals', message= 'Set defaultResolution pixelAspect: 1', verbose = False)

    ## load mentalray
    if not cmds.pluginInfo( 'Mayatomr', query=True, loaded = True ):
        cmds.loadPlugin('Mayatomr')
        debug(app = None, method = 'utils._setRenderGlobals', message= 'Loaded Mayatomr plugin..', verbose = False)

    cmds.setAttr('defaultRenderGlobals.currentRenderer','mentalRay', type = 'string')
    debug(app = None, method = 'utils._setRenderGlobals', message= 'Set currentRenderer to mentalRay', verbose = False)
    mel.eval('unifiedRenderGlobalsWindow;')
    debug(app = None, method = 'utils._setRenderGlobals', message= 'unifiedRenderGlobalsWindow', verbose = False)

    # Default Render Globals
    # /////////////////////
    cmds.setAttr('defaultRenderGlobals.imageFormat', 51)
    debug(app = None, method = 'utils._setRenderGlobals', message= 'defaultRenderGlobals.imageFormat: 51', verbose = False)

    cmds.setAttr('defaultRenderGlobals.imfkey','exr', type = 'string')
    debug(app = None, method = 'utils._setRenderGlobals', message= 'defaultRenderGlobals.imfkey: exr', verbose = False)

    cmds.setAttr('defaultRenderGlobals.animation', 1)
    debug(app = None, method = 'utils._setRenderGlobals', message= 'defaultRenderGlobals.animation: 1', verbose = False)

    cmds.setAttr('defaultRenderGlobals.extensionPadding', 3)
    debug(app = None, method = 'utils._setRenderGlobals', message= 'defaultRenderGlobals.extensionPadding: 3', verbose = False)

    cmds.getAttr('defaultRenderGlobals.extensionPadding')

    cmds.setAttr('defaultRenderGlobals.periodInExt', 1)
    debug(app = None, method = 'utils._setRenderGlobals', message= 'defaultRenderGlobals.periodInExt: 1', verbose = False)

    cmds.setAttr('defaultRenderGlobals.outFormatControl', 0)
    debug(app = None, method = 'utils._setRenderGlobals', message= 'defaultRenderGlobals.outFormatControl: 0', verbose = False)

    cmds.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
    debug(app = None, method = 'utils._setRenderGlobals', message= 'defaultRenderGlobals.putFrameBeforeExt: 1', verbose = False)

    cmds.setAttr('defaultRenderGlobals.enableDefaultLight', 0)
    debug(app = None, method = 'utils._setRenderGlobals', message= 'defaultRenderGlobals.enableDefaultLight: 0', verbose = False)

    cmds.setAttr('defaultResolution.aspectLock', 0)
    debug(app = None, method = 'utils._setRenderGlobals', message= 'defaultRenderGlobals.aspectLock: 0', verbose = False)

    # MentalRay Globals
    # /////////////////////
    cmds.setAttr('mentalrayGlobals.imageCompression', 4)
    cmds.setAttr('mentalrayGlobals.exportPostEffects', 0)
    cmds.setAttr('mentalrayGlobals.accelerationMethod', 4)
    cmds.setAttr('mentalrayGlobals.exportVerbosity', 5)
    # miDefault Frame Buffer
    cmds.setAttr('miDefaultFramebuffer.datatype', 16)
    # miDefault sampling defaults
    cmds.setAttr('miDefaultOptions.filterWidth', 0.6666666667)
    cmds.setAttr('miDefaultOptions.filterHeight', 0.6666666667)
    cmds.setAttr('miDefaultOptions.filter', 2)
    cmds.setAttr('miDefaultOptions.sampleLock', 0)
    # enable raytracing, disable scanline
    cmds.setAttr('miDefaultOptions.scanline', 0)
    try:
        cmds.optionMenuGrp('miSampleModeCtrl', edit = True,  select = 2)
    except:
        pass
    cmds.setAttr('miDefaultOptions.minSamples', -2)
    cmds.setAttr('miDefaultOptions.maxSamples', 0)

    # set sampling quality for RGB channel to eliminate noise
    # costs a bit extra time because it will sample more in the
    # red / green channel but will be faster for blue.
    # using unified sampling
    cmds.setAttr('miDefaultOptions.contrastR', 0.04)
    cmds.setAttr('miDefaultOptions.contrastG', 0.03)
    cmds.setAttr('miDefaultOptions.contrastB', 0.06)
    cmds.setAttr('miDefaultOptions.contrastA', 0.03)

    cmds.setAttr('miDefaultOptions.maxReflectionRays', 3)
    cmds.setAttr('miDefaultOptions.maxRefractionRays', 3)
    cmds.setAttr('miDefaultOptions.maxRayDepth', 5)
    cmds.setAttr('miDefaultOptions.maxShadowRayDepth', 5)

    cmds.setAttr('miDefaultOptions.finalGatherRays', 20)
    cmds.setAttr('miDefaultOptions.finalGatherPresampleDensity', 0.2)
    cmds.setAttr('miDefaultOptions.finalGatherTraceDiffuse', 0)
    cmds.setAttr('miDefaultOptions.finalGatherPoints', 50)

    cmds.setAttr('miDefaultOptions.displacePresample', 0)

    playStart  = cmds.playbackOptions( query = True, minTime= True)
    playFinish = cmds.playbackOptions( query = True, maxTime= True)
    cmds.setAttr('defaultRenderGlobals.startFrame', playStart)
    cmds.setAttr('defaultRenderGlobals.endFrame', playFinish)

    # MentalCore
    # /////////////////////
    if not animation:
        try:
            mapi.enable(True)
            cmds.setAttr('mentalcoreGlobals.en_colour_management',1)
            mel.eval('unifiedRenderGlobalsWindow;')

            cmds.setAttr('mentalcoreGlobals.contrast_all_buffers', 1)

            cmds.setAttr('mentalcoreGlobals.output_mode', 0)
            cmds.setAttr('mentalcoreGlobals.unified_sampling', 1)
            cmds.setAttr('mentalcoreGlobals.samples_min', 1)
            cmds.setAttr('mentalcoreGlobals.samples_max', 80)
            cmds.setAttr('mentalcoreGlobals.samples_quality', 0.8)
            cmds.setAttr('mentalcoreGlobals.samples_error_cutoff', 0.02)

            cmds.setAttr('mentalcoreGlobals.en_envl', 1)
            cmds.setAttr('mentalcoreGlobals.envl_scale', 0.5)
            cmds.setAttr('mentalcoreGlobals.envl_blur_res', 0)
            cmds.setAttr('mentalcoreGlobals.envl_blur', 0)
            cmds.setAttr('mentalcoreGlobals.envl_en_flood_colour', 1)
            cmds.setAttr('mentalcoreGlobals.envl_flood_colour', 1, 1, 1, 1, type = 'double3')
            cmds.setAttr('mentalcoreGlobals.en_ao', 1)
            cmds.setAttr('mentalcoreGlobals.ao_samples', 24)
            cmds.setAttr('mentalcoreGlobals.ao_spread', 60)
            cmds.setAttr('mentalcoreGlobals.ao_near_clip', 1)
            cmds.setAttr('mentalcoreGlobals.ao_far_clip', 10)
            cmds.setAttr('mentalcoreGlobals.ao_opacity', 0)
            cmds.setAttr('mentalcoreGlobals.ao_vis_indirect', 0)
            cmds.setAttr('mentalcoreGlobals.ao_vis_refl', 0)
            cmds.setAttr('mentalcoreGlobals.ao_vis_refr', 1)
            cmds.setAttr('mentalcoreGlobals.ao_vis_trans', 1)
        except:
            cmds.warning('NO MENTAL CORE LOADED!!!')
            pass

        # Default Resolution
        cmds.setAttr('defaultResolution.width', 1280)
        cmds.setAttr('defaultResolution.height', 720)
        cmds.setAttr('defaultResolution.pixelAspect', 1)
        cmds.setAttr('defaultResolution.deviceAspectRatio', 1.7778)
        print 'Default render settings initialized.'