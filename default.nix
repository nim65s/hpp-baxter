{
  lib,
  cmake,
  jrl-cmakemodules,
  python3Packages,
}:

python3Packages.buildPythonPackage {
  pname = "hpp-baxter";
  version = "5.0.0";
  pyproject = false;

  src = lib.fileset.toSource {
    root = ./.;
    fileset = lib.fileset.unions [
      ./CMakeLists.txt
      ./package.xml
      ./src
      ./srdf
      ./urdf
    ];
  };

  strictDeps = true;

  nativeBuildInputs = [ cmake ];
  propagatedBuildInputs = [
    jrl-cmakemodules
    python3Packages.boost
    python3Packages.eigenpy
    python3Packages.example-robot-data
    python3Packages.pinocchio
  ];

  doCheck = true;

  meta = {
    description = "Wrappers for Baxter robot in HPP";
    homepage = "https://github.com/humanoid-path-planner/hpp-baxter";
    license = lib.licenses.bsd2;
    maintainers = [ lib.maintainers.nim65s ];
  };
}
