{
  description = "Wrappers for Baxter robot in HPP";

  inputs.gepetto.url = "github:gepetto/nix";

  outputs =
    inputs:
    inputs.gepetto.lib.mkFlakoboros inputs (
      { lib, ... }:
      {
        overrideAttrs.hpp-baxter = {
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
        };
      }
    );
}
