/// DO NOT EDIT. This is code generated via flutter_gen

import 'package:get/get.dart';
import 'package:{{ package_name }}/scenes/app/app_pages.dart';
{% for file in import_files %}
import '{{ file }}';
{% endfor %}

abstract class AppRouter {
  void reset();
  void back({int? id});
  void backToRoot({int? id});
  {% for item in items %}
  {% if item.is_include_args %}
  Future? to{{ item.class_name }}({{ item.class_name }}Args args, {int? id});
  Future? offAll{{ item.class_name }}({{ item.class_name }}Args args, {int? id});
  Future? offAndTo{{ item.class_name }}({{ item.class_name }}Args args, {int? id});
  Future? off{{ item.class_name }}({{ item.class_name }}Args args, {int? id});
  Future? offUntil{{ item.class_name }}({{ item.class_name }}Args args, {int? id});
  {% else %}
  Future? to{{ item.class_name }}({int? id});
  Future? offAll{{ item.class_name }}({int? id});
  Future? offAndTo{{ item.class_name }}({int? id});
  Future? off{{ item.class_name }}({int? id});
  Future? offUntil{{ item.class_name }}({int? id});
  {% endif %}
  {% endfor %}
}

class AppRouterImpl implements AppRouter {
  @override
  void reset() {
    Get.offAllNamed(Routes.INITIAL);
  }

  @override
  void back({int? id}) {
    Get.back(id: id);
  }

  @override
  void backToRoot({int? id}) {
    Get.until((route) => route.isFirst, id: id);
  }

  {% for item in items %}
  {% if item.is_include_args %}
  @override
  Future? to{{ item.class_name }}({{ item.class_name }}Args args, {int? id}) {
    return Get.toNamed(Routes.{{ item.route_name }}, arguments: args, id: id);
  }

  @override
  Future? offAll{{ item.class_name }}({{ item.class_name }}Args args, {int? id}) {
    return Get.offAllNamed(Routes.{{ item.route_name }}, arguments: args, id: id);
  }

  @override
  Future? offAndTo{{ item.class_name }}({{ item.class_name }}Args args, {int? id}) {
    return Get.offAndToNamed(Routes.{{ item.route_name }}, arguments: args, id: id);
  }

  @override
  Future? off{{ item.class_name }}({{ item.class_name }}Args args, {int? id}) {
    return Get.offNamed(Routes.{{ item.route_name }}, arguments: args, id: id);
  }

  @override
  Future? offUntil{{ item.class_name }}({{ item.class_name }}Args args, {int? id}) {
    return Get.offNamedUntil(Routes.{{ item.route_name }}, (_) => false, arguments: args, id: id);
  }

  {% else %}
  @override
  Future? to{{ item.class_name }}({int? id}) {
    return Get.toNamed(Routes.{{ item.route_name }}, id: id);
  }

  @override
  Future? offAll{{ item.class_name }}({int? id}) {
    return Get.offAllNamed(Routes.{{ item.route_name }}, id: id);
  }

  @override
  Future? offAndTo{{ item.class_name }}({int? id}) {
    return Get.offAndToNamed(Routes.{{ item.route_name }}, id: id);
  }

  @override
  Future? off{{ item.class_name }}({int? id}) {
    return Get.offNamed(Routes.{{ item.route_name }}, id: id);
  }

  @override
  Future? offUntil{{ item.class_name }}({int? id}) {
    return Get.offNamedUntil(Routes.{{ item.route_name }}, (_) => false, id: id);
  }

  {% endif %}
  {% endfor %}
}
