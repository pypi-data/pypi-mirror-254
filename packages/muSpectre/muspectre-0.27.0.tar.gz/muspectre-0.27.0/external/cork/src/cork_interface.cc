#include "cork_interface.hh"

namespace corkpp {

void file2corktrimesh(const Files::FileMesh &in, CorkTriMesh &out) {
  out.n_vertices = in.vertices.size();
  out.n_triangles = in.triangles.size();

  out.triangles.resize(out.n_triangles * 3);
  out.vertices.resize(out.n_triangles * 3);

  for (uint i = 0; i < out.n_triangles; i++) {
    (out.triangles)[3 * i + 0] = in.triangles[i].a;
    (out.triangles)[3 * i + 1] = in.triangles[i].b;
    (out.triangles)[3 * i + 2] = in.triangles[i].c;
  }

  for (uint i = 0; i < out.n_vertices; i++) {
    (out.vertices)[3 * i + 0] = in.vertices[i].pos.x;
    (out.vertices)[3 * i + 1] = in.vertices[i].pos.y;
    (out.vertices)[3 * i + 2] = in.vertices[i].pos.z;
  }
}

void corktrimesh2file(CorkTriMesh in, Files::FileMesh &out) {
  out.vertices.resize(in.n_vertices);
  out.triangles.resize(in.n_triangles);

  for (uint i = 0; i < in.n_triangles; i++) {
    out.triangles[i].a = in.triangles[3 * i + 0];
    out.triangles[i].b = in.triangles[3 * i + 1];
    out.triangles[i].c = in.triangles[3 * i + 2];
  }

  for (uint i = 0; i < in.n_vertices; i++) {
    out.vertices[i].pos.x = in.vertices[3 * i + 0];
    out.vertices[i].pos.y = in.vertices[3 * i + 1];
    out.vertices[i].pos.z = in.vertices[3 * i + 2];
  }
}

void loadMesh(string filename, CorkTriMesh &out) {
  Files::FileMesh filemesh;

  if (Files::readTriMesh(filename, &filemesh) > 0) {
    cerr << "Unable to load in " << filename << endl;
    exit(1);
  }

  file2corktrimesh(filemesh, out);
}
void saveMesh(string filename, CorkTriMesh in) {
  Files::FileMesh filemesh;

  corktrimesh2file(in, filemesh);

  if (Files::writeTriMesh(filename, &filemesh) > 0) {
    cerr << "Unable to write to " << filename << endl;
    exit(1);
  }
}

/*-----------------------------------------------------------------------------*/

auto calculate_intersection_volume_normal_state(
    const std::vector<point_t> vertices_precipitate,
    const std::vector<point_t> vertices_pixel, int dim)
    -> VolNormStateIntersection {
  std::vector<face_t> faces_precipitate, faces_pixel;
  VolNormStateIntersection ret_structure;
  make_faces_from_nodes(vertices_precipitate, faces_precipitate);
  make_faces_from_nodes(vertices_pixel, faces_pixel);
  CorkTriMesh precipitate;
  CorkTriMesh pixel;
  CorkTriMesh intersection;
  CorkTriMesh difference;
  CorkTriMesh intersection_and_difference;
  corktrimesh_maker_from_node_faces(vertices_precipitate, faces_precipitate,
                                    precipitate);
  corktrimesh_maker_from_node_faces(vertices_pixel, faces_pixel, pixel);

  compute_intersection(precipitate, pixel, intersection);

  ret_structure.volume = volume_calculator(intersection);
  ret_structure.volume_ratio = ret_structure.volume / volume_calculator(pixel);

  // computeDifference(pixel, precipitate, difference);
  // intersect_of_faces(intersection, difference,
  // intersection_and_difference);
  diff_of_faces(intersection, pixel, intersection_and_difference);
  ret_structure.normal_vector =
      average_normal_calculator(intersection_and_difference);
  auto &&vol_precipitate = volume_calculator(precipitate);
  set_intersection_state(ret_structure, vol_precipitate, dim);
  return ret_structure;
}

/*-----------------------------------------------------------------------------*/

auto calculate_intersection_volume_state(
    const std::vector<point_t> vertices_precipitate,
    const std::vector<point_t> vertices_pixel, int dim)
    -> VolStateIntersection {
  std::vector<face_t> faces_precipitate, faces_pixel;
  VolNormStateIntersection complete_structure;
  VolStateIntersection ret_structure;
  make_faces_from_nodes(vertices_precipitate, faces_precipitate);
  make_faces_from_nodes(vertices_pixel, faces_pixel);
  CorkTriMesh precipitate;
  CorkTriMesh pixel;
  CorkTriMesh intersection;
  CorkTriMesh difference;
  CorkTriMesh intersection_and_difference;
  corktrimesh_maker_from_node_faces(vertices_precipitate, faces_precipitate,
                                    precipitate);
  corktrimesh_maker_from_node_faces(vertices_pixel, faces_pixel, pixel);

  compute_intersection(precipitate, pixel, intersection);

  ret_structure.volume = volume_calculator(intersection);
  ret_structure.volume_ratio = ret_structure.volume / volume_calculator(pixel);
  complete_structure.volume = ret_structure.volume;
  complete_structure.volume_ratio = ret_structure.volume_ratio;
  // computeDifference(pixel, precipitate, difference);
  // intersect_of_faces(intersection, difference,
  // intersection_and_difference);
  diff_of_faces(intersection, pixel, intersection_and_difference);
  auto &&vol_precipitate = volume_calculator(precipitate);
  complete_structure.normal_vector =
      average_normal_calculator(intersection_and_difference);
  set_intersection_state(complete_structure, vol_precipitate, dim);
  ret_structure.status = complete_structure.status;
  return ret_structure;
}

/*-----------------------------------------------------------------------------*/
auto calculate_intersection_volume(
    const std::vector<point_t> vertices_precipitate,
    const std::vector<point_t> vertices_pixel) -> REal {
  std::vector<face_t> faces_precipitate, faces_pixel;
  make_faces_from_nodes(vertices_precipitate, faces_precipitate);
  make_faces_from_nodes(vertices_pixel, faces_pixel);
  CorkTriMesh precipitate;
  CorkTriMesh pixel;
  corktrimesh_maker_from_node_faces(vertices_precipitate, faces_precipitate,
                                    precipitate);
  corktrimesh_maker_from_node_faces(vertices_pixel, faces_pixel, pixel);

  CorkTriMesh intersection;
  compute_intersection(precipitate, pixel, intersection);
  auto &&vol = volume_calculator(intersection);
  return vol;
}

/*-----------------------------------------------------------------------------*/
void CokrTriMesh_maker(const std::vector<point_t> &precipitate_vertices,
                       const std::vector<face_t> &faces, CorkTriMesh &out) {
  out.n_vertices = precipitate_vertices.size();
  out.n_triangles = faces.size();

  out.vertices.resize(3 * out.n_vertices);
  out.triangles.resize(3 * out.n_triangles);

  point_t tmp_point;
  face_t tmp_face;
  for (uint i = 0; i < faces.size(); ++i) {
    tmp_face = faces[i];
    (out.triangles)[3 * i + 0] = tmp_face[0];
    (out.triangles)[3 * i + 1] = tmp_face[1];
    (out.triangles)[3 * i + 2] = tmp_face[2];
  }
  for (uint i = 0; i < precipitate_vertices.size(); i++) {
    tmp_point = precipitate_vertices[i];
    (out.vertices)[3 * i + 0] = tmp_point[0];
    (out.vertices)[3 * i + 1] = tmp_point[1];
    (out.vertices)[3 * i + 2] = tmp_point[2];
  }
}

/*----------------------------------------------------------------------------*/
vector_t average_normal_calculator(const CorkTriMesh &in) {
  double total_area = 0.0, face_area = 0.0;
  vector_t total_face_normal_time_area;
  total_face_normal_time_area << 0.0, 0.0, 0.0;
  face_t face;
  std::vector<point_t> vertices(in.n_vertices, {0.0, 0.0, 0.0});
  for (uint i = 0; i < in.n_vertices; ++i) {
    vertices[i] = {in.vertices[3 * i + 0], in.vertices[3 * i + 1],
                   in.vertices[3 * i + 2]};
  }
  for (uint i = 0; i < in.n_triangles; ++i) {
    face = {in.triangles[3 * i + 0], in.triangles[3 * i + 1],
            in.triangles[3 * i + 2]};
    face_area = face_area_calculator(vertices, face);
    total_area += face_area;
    total_face_normal_time_area +=
        face_area * face_normal_calculator(vertices, face);
  }
  total_face_normal_time_area = total_face_normal_time_area / total_area;

  for (int i = 0; i < total_face_normal_time_area.size(); ++i) {
    if (std::abs(total_face_normal_time_area[i]) < tolerance) {
      total_face_normal_time_area[i] = 0.0;
    }
  }

  return total_face_normal_time_area.normalized();
}
/*-----------------------------------------------------------------------------*/
vector_t face_normal_calculator(const std::vector<point_t> &vertices,
                                const face_t &face) {
  std::array<vector_t, 3> face_vertices;
  for (int i = 0; i < 3; ++i) {
    face_vertices[i] << vertices[face[i]][0], vertices[face[i]][1],
        vertices[face[i]][2];
  }
  return (face_vertices[1] - face_vertices[0])
      .cross(face_vertices[2] - face_vertices[1])
      .normalized()
      .derived();
}
/*-----------------------------------------------------------------------------*/
double face_area_calculator(const std::vector<point_t> &vertices,
                            const face_t &face) {
  std::array<vector_t, 3> face_vertices;
  for (int i = 0; i < 3; ++i) {
    face_vertices[i] << vertices[face[i]][0], vertices[face[i]][1],
        vertices[face[i]][2];
  }

  return ((face_vertices[1] - face_vertices[0])
              .cross(face_vertices[2] - face_vertices[1])
              .norm()) /
         2;
}
/*-----------------------------------------------------------------------------*/
auto face_constant_calculator(const std::vector<point_t> &vertices,
                              const face_t &face, vector_t normal) -> double {
  vector_t vertice;
  vertice << vertices[face[0]][0], vertices[face[0]][1], vertices[face[0]][2];
  return (-vertice.dot(normal.normalized()));
}
/*-----------------------------------------------------------------------------*/
vector_t a_point_polyhedron_claculator(const std::vector<point_t> &vertices) {
  vector_t vertice1;
  vertice1 << vertices[0][0], vertices[0][1], vertices[0][2];
  vector_t vertice2;
  vertice2 << vertices[0][0], vertices[1][1], vertices[1][2];
  return (vertice1 + vertice2) / 2;
};
/*-----------------------------------------------------------------------------*/
double volume_calculator(const CorkTriMesh &in) {
  double ret_volume = 0.0;
  double face_area;
  vector_t face_normal;
  double face_constant;
  double face_height;
  face_t face;
  std::vector<point_t> vertices(in.n_vertices, {0.0, 0.0, 0.0});
  for (uint i = 0; i < in.n_vertices; ++i) {
    vertices[i] = {in.vertices[3 * i + 0], in.vertices[3 * i + 1],
                   in.vertices[3 * i + 2]};
  }
  if (vertices.size() == 0.0) {
    return 0;
  }
  vector_t point_inside{a_point_polyhedron_claculator(vertices)};
  for (uint i = 0; i < in.n_triangles; ++i) {
    face = {in.triangles[3 * i + 0], in.triangles[3 * i + 1],
            in.triangles[3 * i + 2]};
    face_area = face_area_calculator(vertices, face);
    face_normal = face_normal_calculator(vertices, face);
    face_constant = face_constant_calculator(vertices, face, face_normal);
    face_height = std::abs(point_plane_distance_calculator(
        point_inside, face_normal, face_constant));
    if (face_normal != Eigen::Vector3d::Zero()) {
      ret_volume += face_area * face_height / 3.0;
    }
  }
  // std::cout << ret_volume << std::endl;
  return ret_volume;
}
/*-----------------------------------------------------------------------------*/
void intersect_of_faces(const CorkTriMesh &in0, const CorkTriMesh &in1,
                        CorkTriMesh &out, REal pixel_size) {
  vector_t normal0;
  normal0 << 0.0, 0.0, 0.0;
  std::vector<vector_t> normals1(in1.n_triangles, normal0);
  point_t vertice{0.0, 0.0, 0.0};
  std::vector<point_t> vertices0(in0.n_vertices, vertice);
  std::vector<point_t> vertices1(in1.n_vertices, vertice);
  std::vector<double> constants1(in1.n_triangles, 0.0);
  double constant0;
  face_t face;
  std::vector<bool> new_face_checker(in0.n_triangles, false);
  // here we calculate the normal and the constants of all facets of in1 and
  // normalize constants by dividing by pixel size;
  for (uint i = 0; i < in1.n_vertices; ++i) {
    vertices1[i] = {in1.vertices[3 * i + 0], in1.vertices[3 * i + 1],
                    in1.vertices[3 * i + 2]};
  }
  for (uint i = 0; i < in1.n_triangles; ++i) {
    face = {in1.triangles[3 * i + 0], in1.triangles[3 * i + 1],
            in1.triangles[3 * i + 2]};
    normals1[i] = face_normal_calculator(vertices1, face);
    constants1[i] =
        face_constant_calculator(vertices1, face, normals1[i]) / pixel_size;
  }
  uint counter1 = 0;
  // here we calculate the normal and the constants of all facets of in0 and
  // loop over all of the facets of the in1 to check their similarity and
  // divide the constant by the size of the pixel
  for (uint i = 0; i < in0.n_vertices; ++i) {
    vertices0[i] = {in0.vertices[3 * i + 0], in0.vertices[3 * i + 1],
                    in0.vertices[3 * i + 2]};
  }

  for (uint i = 0; i < in0.n_triangles; ++i) {
    face = {in0.triangles[3 * i + 0], in0.triangles[3 * i + 1],
            in0.triangles[3 * i + 2]};
    normal0 = face_normal_calculator(vertices0, face);
    constant0 = face_constant_calculator(vertices0, face, normal0) / pixel_size;
    for (uint j = 0; j < in1.n_triangles; ++j) {
      if (std::abs(constants1[j] - constant0) < tolerance) {
        for (uint k = 0; k < 3; ++k) {
          if (std::abs(normals1[j][k] - normal0[k]) < tolerance) {
            counter1++;
          }
        }
        if (counter1 == 3) {
          new_face_checker[i] = true;
        }
        counter1 = 0;
      }
    }
  }

  uint counter = 0;
  out.n_vertices = in0.n_vertices;
  out.n_triangles =
      std::count(new_face_checker.begin(), new_face_checker.end(), true);

  out.vertices.resize(3 * out.n_vertices);
  out.triangles.resize(3 * out.n_triangles);
  out.vertices = in0.vertices;
  for (uint i = 0; i < in0.n_triangles; ++i) {
    if (new_face_checker[i]) {
      (out.triangles)[3 * counter + 0] = in0.triangles[3 * i + 0];
      (out.triangles)[3 * counter + 1] = in0.triangles[3 * i + 1];
      (out.triangles)[3 * counter + 2] = in0.triangles[3 * i + 2];
      counter++;
    }
  }
}

/*-----------------------------------------------------------------------------*/
void diff_of_faces(const CorkTriMesh &in0, const CorkTriMesh &in1,
                   CorkTriMesh &out, REal pixel_size) {
  vector_t normal0;
  normal0 << 0.0, 0.0, 0.0;
  point_t vertice{0.0, 0.0, 0.0};

  std::vector<point_t> vertices0(in0.n_vertices, vertice);
  std::vector<point_t> vertices1(in1.n_vertices, vertice);

  std::vector<double> constants1(in1.n_triangles, 0.0);
  std::vector<vector_t> normals1(in1.n_triangles, normal0);

  double constant0;
  face_t face;

  std::vector<bool> new_face_checker(in0.n_triangles, true);

  // here we calculate the normal and the constants of all facets of in1 (pixel)
  for (uint i = 0; i < in1.n_vertices; ++i) {
    vertices1[i] = {in1.vertices[3 * i + 0], in1.vertices[3 * i + 1],
                    in1.vertices[3 * i + 2]};
  }
  for (uint i = 0; i < in1.n_triangles; ++i) {
    face = {in1.triangles[3 * i + 0], in1.triangles[3 * i + 1],
            in1.triangles[3 * i + 2]};
    normals1[i] = face_normal_calculator(vertices1, face);
    constants1[i] = face_constant_calculator(vertices1, face, normals1[i]);
  }
  //

  uint counter1 = 0;
  // here we calculate the normal and the constants of all facets of in0
  // (intersection) and loop over all of the facets of the in1 to check their
  // similarity
  for (uint i = 0; i < in0.n_vertices; ++i) {
    vertices0[i] = {in0.vertices[3 * i + 0], in0.vertices[3 * i + 1],
                    in0.vertices[3 * i + 2]};
  }

  for (uint i = 0; i < in0.n_triangles; ++i) {
    face = {in0.triangles[3 * i + 0], in0.triangles[3 * i + 1],
            in0.triangles[3 * i + 2]};
    normal0 = face_normal_calculator(vertices0, face);
    constant0 = face_constant_calculator(vertices0, face, normal0);
    for (uint j = 0; j < in1.n_triangles; ++j) {
      if ((std::abs(constant0) + std::abs(constants1[j])) < tolerance or
          std::abs(2 * (constants1[j] - constant0) /
                   (std::abs(constant0) + std::abs(constants1[j]))) <
              tolerance) {
        for (uint k = 0; k < 3; ++k) {
          if (std::abs(normals1[j][k] - normal0[k]) < tolerance) {
            counter1++;
          }
        }
        if (counter1 == 3) {
          new_face_checker[i] = false;
        }
        counter1 = 0;
      }
    }
  }

  uint counter = 0;
  out.n_triangles =
      std::count(new_face_checker.begin(), new_face_checker.end(), true);
  if (out.n_triangles != 0) {
    out.n_vertices = in0.n_vertices;
    out.vertices.resize(3 * out.n_vertices);
    out.triangles.resize(3 * out.n_triangles);
    out.vertices = in0.vertices;
    for (uint i = 0; i < in0.n_triangles; ++i) {
      if (new_face_checker[i]) {
        out.triangles[3 * counter + 0] = in0.triangles[3 * i + 0];
        out.triangles[3 * counter + 1] = in0.triangles[3 * i + 1];
        out.triangles[3 * counter + 2] = in0.triangles[3 * i + 2];
        counter++;
      }
    }
  }

  // std::cout << counter << std::endl;
}
/*-----------------------------------------------------------------------------*/
std::vector<point_t> cube_vertice_maker(point_t origin, point_t size) {
  std::vector<point_t> ret_vertices(8, {0.0, 0.0, 0.0});
  ret_vertices[0] = {origin[0], origin[1], origin[2]};
  ret_vertices[1] = {origin[0] + size[0], origin[1], origin[2]};
  ret_vertices[2] = {origin[0], origin[1] + size[1], origin[2]};
  ret_vertices[6] = {origin[0], origin[1], origin[2] + size[2]};
  ret_vertices[4] = {origin[0], origin[1] + size[1], origin[2] + size[2]};
  ret_vertices[5] = {origin[0] + size[0], origin[1], origin[2] + size[2]};
  ret_vertices[3] = {origin[0] + size[0], origin[1] + size[1], origin[2]};
  ret_vertices[7] = {origin[0] + size[0], origin[1] + size[1],
                     origin[2] + size[2]};
  return ret_vertices;
}
/*-----------------------------------------------------------------------------*/
void corktrimesh_maker_from_node_faces(
    const std::vector<point_t> &precipitate_vertices,
    const std::vector<face_t> &faces, CorkTriMesh &out) {
  out.n_vertices = precipitate_vertices.size();
  out.n_triangles = faces.size();
  out.vertices.resize(3 * out.n_vertices);
  out.triangles.resize(3 * out.n_triangles);

  point_t tmp_point;
  // face_t tmp_face;
  for (uint i = 0; i < faces.size(); ++i) {
    // tmp_face = faces[i];
    out.triangles[3 * i + 0] = faces[i][0];
    out.triangles[3 * i + 1] = faces[i][1];
    out.triangles[3 * i + 2] = faces[i][2];
  }
  for (uint i = 0; i < precipitate_vertices.size(); i++) {
    tmp_point = precipitate_vertices[i];
    out.vertices[3 * i + 0] = tmp_point[0];
    out.vertices[3 * i + 1] = tmp_point[1];
    out.vertices[3 * i + 2] = tmp_point[2];
  }
}
/*-----------------------------------------------------------------------------*/
void compute_intersection(const CorkTriMesh &in0, const CorkTriMesh &in1,
                          CorkTriMesh &out) {
  int iter{0};
  ResultState state{ResultState::solid};
  do {
    pseudoInitRand(iter++);
    computeIntersection(in0, in1, out);
    state = checkState(out);
  } while (state == ResultState::non_solid);
  if (state == ResultState::empty and iter > 0) {
    do {
      pseudoInitRand(iter++);
      computeIntersection(in0, in1, out);
      state = checkState(out);
    } while (state == ResultState::non_solid);
  }
}

/*-----------------------------------------------------------------------------*/
void compute_difference(const CorkTriMesh &in0, const CorkTriMesh &in1,
                        CorkTriMesh &out) {
  int iter{0};
  ResultState state{ResultState::solid};
  do {
    pseudoInitRand(iter++);
    computeDifference(in0, in1, out);
    state = checkState(out);
  } while (state == ResultState::non_solid);
  if (state == ResultState::empty and iter > 0) {
    do {
      pseudoInitRand(iter++);
      computeIntersection(in0, in1, out);
      state = checkState(out);
    } while (state == ResultState::non_solid);
  }
}
/*-----------------------------------------------------------------------------*/

void set_intersection_state(VolNormStateIntersection &intersection,
                            REal vol_precipitate, int dim) {
  if (intersection.volume_ratio < tolerance_ratio) {
    intersection.status = IntersectionState::non_intersecting;
  } else if (intersection.volume_ratio > 1 - tolerance_ratio) {
    intersection.status = IntersectionState::enclosing;
  } else if (intersection.normal_vector.head(dim).norm() == 0.0) {
    intersection.status = IntersectionState::completely_inside;
  }
}
/*-----------------------------------------------------------------------------*/

} // namespace corkpp
