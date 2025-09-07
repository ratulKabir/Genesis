import genesis as gs

def build_env():
    entities = {}

    gs.init()

    scene = gs.Scene(show_viewer=True,)

    entities["plane"] = scene.add_entity(
        gs.morphs.Plane(),
    )

    entities["robot"] = scene.add_entity(
        material=gs.materials.Rigid(gravity_compensation=1),
        morph=gs.morphs.MJCF(
            file="/Users/ratul/Workstation/github_repos/LeKiwi-sim/configs/mjcf_lcmm_robot.xml",
            euler=(0, 0, 0),
        ),
    )

    scene.build()

    return scene, entities

if __name__ == "__main__":
    scene, entities = build_env()

    for _i in range(1000):
        scene.step()
