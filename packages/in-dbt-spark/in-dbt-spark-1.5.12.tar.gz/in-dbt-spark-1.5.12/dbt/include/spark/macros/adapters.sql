{% macro dbt_spark_tblproperties_clause() -%}
  {%- set tblproperties = config.get('tblproperties') -%}
  {%- if tblproperties is not none %}
    tblproperties (
      {%- for prop in tblproperties -%}
      '{{ prop }}' = '{{ tblproperties[prop] }}' {% if not loop.last %}, {% endif %}
      {%- endfor %}
    )
  {%- endif %}
{%- endmacro -%}

{% macro file_format_clause() %}
  {{ return(adapter.dispatch('file_format_clause', 'dbt')()) }}
{%- endmacro -%}

{% macro spark__file_format_clause() %}
  {%- set file_format = config.get('file_format', validator=validation.any[basestring]) -%}
  {%- if file_format is not none %}
    using {{ file_format }}
  {%- endif %}
{%- endmacro -%}


{% macro location_clause() %}
  {{ return(adapter.dispatch('location_clause', 'dbt')()) }}
{%- endmacro -%}

{% macro spark__location_clause() %}
  {%- set location_root = config.get('location_root', validator=validation.any[basestring]) -%}
  {%- set identifier = model['alias'] -%}
  {%- if location_root is not none %}
    location '{{ location_root }}/{{ identifier }}'
  {%- endif %}
{%- endmacro -%}


{% macro options_clause() -%}
  {{ return(adapter.dispatch('options_clause', 'dbt')()) }}
{%- endmacro -%}

{% macro spark__options_clause() -%}
  {%- set options = config.get('options') -%}
  {%- if config.get('file_format') == 'hudi' -%}
    {%- set unique_key = config.get('unique_key') -%}
    {%- if unique_key is not none and options is none -%}
      {%- set options = {'primaryKey': config.get('unique_key')} -%}
    {%- elif unique_key is not none and options is not none and 'primaryKey' not in options -%}
      {%- set _ = options.update({'primaryKey': config.get('unique_key')}) -%}
    {%- elif options is not none and 'primaryKey' in options and options['primaryKey'] != unique_key -%}
      {{ exceptions.raise_compiler_error("unique_key and options('primaryKey') should be the same column(s).") }}
    {%- endif %}
  {%- endif %}

  {%- if options is not none %}
    options (
      {%- for option in options -%}
      {{ option }} "{{ options[option] }}" {% if not loop.last %}, {% endif %}
      {%- endfor %}
    )
  {%- endif %}
{%- endmacro -%}


{% macro comment_clause() %}
  {{ return(adapter.dispatch('comment_clause', 'dbt')()) }}
{%- endmacro -%}

{% macro spark__comment_clause() %}
  {%- set raw_persist_docs = config.get('persist_docs', {}) -%}

  {%- if raw_persist_docs is mapping -%}
    {%- set raw_relation = raw_persist_docs.get('relation', true) -%}
    {%- if raw_relation and model.description|length -%}
      comment '{{ model.description | replace("'", "\\'") }}'
    {% endif %}
  {%- elif raw_persist_docs -%}
    {{ exceptions.raise_compiler_error("Invalid value provided for 'persist_docs'. Expected dict but got value: " ~ raw_persist_docs) }}
  {% endif %}
{%- endmacro -%}


{% macro set_dbt_tblproperties(relation, model) %}
  {{ return(adapter.dispatch('set_dbt_tblproperties', 'dbt')(relation, model)) }}
{%- endmacro -%}

{% macro spark__set_dbt_tblproperties(relation, model) %}
  {%- set mp_name = var('MULTIPRODUCT_NAME', None) -%}
  {%- set project_name = model.package_name -%}
  {%- set model_name = model.name -%}

  {% if target.name == 'prod' and config.get('file_format', 'openhouse') == 'openhouse' %}
    {% set set_tblproperties_query %}
        {% if mp_name is not none %}
            alter table {{ relation }} set tblproperties ('dbt.mp_name'='{{ mp_name }}',
                                                            'dbt.project_name'='{{ project_name }}',
                                                            'dbt.model_name'='{{ model_name }}');
        {% else %}
            alter table {{ relation }} set tblproperties ('dbt.project_name'='{{ project_name }}',
                                                            'dbt.model_name'='{{ model_name }}');
        {% endif %}
    {% endset %}
    {% do run_query(set_tblproperties_query) %}
  {% endif %}
{% endmacro %}


{% macro partition_cols(label, required=false) %}
  {{ return(adapter.dispatch('partition_cols', 'dbt')(label, required)) }}
{%- endmacro -%}

{% macro spark__partition_cols(label, required=false) %}
  {%- set raw_partition_by = config.get('partition_by', validator=validation.any[list, dict]) -%}
  {%- set file_format = config.get('file_format', validator=validation.any[basestring]) -%}

  {%- if raw_partition_by is not none %}
    {{ label }} (
    {%- set partition_by_list = adapter.parse_partition_by(raw_partition_by) -%}
    {%- for partition_by in partition_by_list -%}
      {%- if file_format == 'openhouse' and partition_by.data_type | lower in ['timestamp'] -%}
        {%- if partition_by.granularity is none -%}
          {% do exceptions.raise_compiler_error("For partitioned tables with file_format = 'openhouse' and data_type = 'timestamp', granularity must be provided") %}
        {%- endif -%}
        {{ partition_by.granularity }}({{ partition_by.field }})
      {%- elif file_format == 'openhouse' and partition_by.data_type | lower in ['string', 'int'] -%}
        {{ partition_by.field }}
      {%- else -%}
        {{ partition_by.field }}
      {%- endif -%}
      {%- if not loop.last -%},{%- endif -%}
    {%- endfor -%}
    )
  {%- endif %}
{%- endmacro -%}

{% macro clustered_cols(label, required=false) %}
  {{ return(adapter.dispatch('clustered_cols', 'dbt')(label, required)) }}
{%- endmacro -%}

{% macro spark__clustered_cols(label, required=false) %}
  {%- set cols = config.get('clustered_by', validator=validation.any[list, basestring]) -%}
  {%- set buckets = config.get('buckets', validator=validation.any[int]) -%}
  {%- if (cols is not none) and (buckets is not none) %}
    {%- if cols is string -%}
      {%- set cols = [cols] -%}
    {%- endif -%}
    {{ label }} (
    {%- for item in cols -%}
      {{ item }}
      {%- if not loop.last -%},{%- endif -%}
    {%- endfor -%}
    ) into {{ buckets }} buckets
  {%- endif %}
{%- endmacro -%}


{% macro fetch_tbl_properties(relation) -%}
  {% call statement('list_properties', fetch_result=True) -%}
    SHOW TBLPROPERTIES {{ relation }}
  {% endcall %}
  {% do return(load_result('list_properties').table) %}
{%- endmacro %}


{% macro create_temporary_view(relation, compiled_code) -%}
  {{ return(adapter.dispatch('create_temporary_view', 'dbt')(relation, compiled_code)) }}
{%- endmacro -%}

{#-- We can't use temporary tables with `create ... as ()` syntax --#}
{% macro spark__create_temporary_view(relation, compiled_code) -%}
    create or replace temporary view {{ relation }} as
      {{ compiled_code }}
{%- endmacro -%}


{%- macro spark__create_table_as(temporary, relation, compiled_code, language='sql') -%}
  {%- if language == 'sql' -%}
    {%- if temporary -%}
      {{ create_temporary_view(relation, compiled_code) }}
    {%- else -%}
      {% if config.get('file_format', validator=validation.any[basestring]) in ['delta', 'iceberg'] %}
        create or replace table {{ relation }}
      {% else %}
        create table {{ relation }}
      {% endif %}
      {%- set contract_config = config.get('contract') -%}
      {%- if contract_config.enforced -%}
        {{ get_assert_columns_equivalent(compiled_code) }}
        {%- set compiled_code = get_select_subquery(compiled_code) %}
      {% endif %}
      {% if config.get('file_format', validator=validation.any[basestring]) != 'openhouse' %}
        {{ file_format_clause() }}
      {% endif %}
      {{ options_clause() }}
      {{ partition_cols(label="partitioned by") }}
      {% if config.get('file_format', validator=validation.any[basestring]) != 'openhouse' %}
        {{ clustered_cols(label="clustered by") }}
        {{ location_clause() }}
      {% endif %}
      {{ comment_clause() }}
      as
      {{ compiled_code }}
    {%- endif -%}
  {%- elif language == 'python' -%}
    {#--
    N.B. Python models _can_ write to temp views HOWEVER they use a different session
    and have already expired by the time they need to be used (I.E. in merges for incremental models)

    TODO: Deep dive into spark sessions to see if we can reuse a single session for an entire
    dbt invocation.
     --#}
    {{ py_write_table(compiled_code=compiled_code, target_relation=relation) }}
  {%- endif -%}
{%- endmacro -%}


{% macro persist_constraints(relation, model) %}
  {{ return(adapter.dispatch('persist_constraints', 'dbt')(relation, model)) }}
{% endmacro %}

{% macro spark__persist_constraints(relation, model) %}
  {%- set contract_config = config.get('contract') -%}
  {% if contract_config.enforced and config.get('file_format', 'delta') == 'delta' %}
    {% do alter_table_add_constraints(relation, model.columns) %}
    {% do alter_column_set_constraints(relation, model.columns) %}
  {% endif %}
{% endmacro %}

{% macro alter_table_add_constraints(relation, constraints) %}
  {{ return(adapter.dispatch('alter_table_add_constraints', 'dbt')(relation, constraints)) }}
{% endmacro %}

{% macro spark__alter_table_add_constraints(relation, column_dict) %}

  {% for column_name in column_dict %}
    {% set constraints = column_dict[column_name]['constraints'] %}
    {% for constraint in constraints %}
      {% if constraint.type == 'check' and not is_incremental() %}
        {%- set constraint_hash = local_md5(column_name ~ ";" ~ constraint.expression ~ ";" ~ loop.index) -%}
        {% call statement() %}
          alter table {{ relation }} add constraint {{ constraint_hash }} check {{ constraint.expression }};
        {% endcall %}
      {% endif %}
    {% endfor %}
  {% endfor %}
{% endmacro %}

{% macro alter_column_set_constraints(relation, column_dict) %}
  {{ return(adapter.dispatch('alter_column_set_constraints', 'dbt')(relation, column_dict)) }}
{% endmacro %}

{% macro spark__alter_column_set_constraints(relation, column_dict) %}
  {% for column_name in column_dict %}
    {% set constraints = column_dict[column_name]['constraints'] %}
    {% for constraint in constraints %}
      {% if constraint.type != 'not_null' %}
        {{ exceptions.warn('Invalid constraint for column ' ~ column_name ~ '. Only `not_null` is supported.') }}
      {% else %}
        {% set quoted_name = adapter.quote(column_name) if column_dict[column_name]['quote'] else column_name %}
        {% call statement() %}
          alter table {{ relation }} change column {{ quoted_name }} set not null {{ constraint.expression or "" }};
        {% endcall %}
      {% endif %}
    {% endfor %}
  {% endfor %}
{% endmacro %}

{% macro spark__create_view_as(relation, sql) -%}
  create or replace view {{ relation }}
  {{ comment_clause() }}
  {%- set contract_config = config.get('contract') -%}
  {%- if contract_config.enforced -%}
    {{ get_assert_columns_equivalent(sql) }}
  {%- endif %}
  as
    {{ sql }}
{% endmacro %}

{% macro spark__create_schema(relation) -%}
  {%- call statement('create_schema') -%}
    {% if '.' in relation.schema %}
      show databases like 'fake_placeholder__create_schema'
    {% else %}
      create schema if not exists {{relation}}
    {% endif %}
  {% endcall %}
{% endmacro %}

{% macro spark__drop_schema(relation) -%}
  {%- call statement('drop_schema') -%}
    {% if '.' in relation.schema %}
      show databases like 'fake_placeholder__drop_schema'
    {% else %}
      drop schema if exists {{ relation }} cascade
    {% endif %}
  {%- endcall -%}
{% endmacro %}

{% macro get_columns_in_relation_raw(relation) -%}
  {{ return(adapter.dispatch('get_columns_in_relation_raw', 'dbt')(relation)) }}
{%- endmacro -%}

{% macro spark__get_columns_in_relation_raw(relation) -%}
  {% call statement('get_columns_in_relation_raw', fetch_result=True) %}
      describe extended {{ relation }}
  {% endcall %}
  {% do return(load_result('get_columns_in_relation_raw').table) %}
{% endmacro %}

{% macro spark__get_columns_in_relation(relation) -%}
  {% call statement('get_columns_in_relation', fetch_result=True) %}
      describe extended {{ relation.include(schema=(schema is not none)) }}
  {% endcall %}
  {% do return(load_result('get_columns_in_relation').table) %}
{% endmacro %}

-- override macro to list only relations related to current dbt project
{% macro spark__list_relations_without_caching(relation) %}
  {% call statement('list_relations_without_caching', fetch_result=True) -%}
    show table extended in {{ relation.schema }} like '{{ relation.identifier or "*" }}'
  {% endcall %}
  {% do return(load_result('list_relations_without_caching').table) %}
{% endmacro %}

{% macro list_relations_show_tables_without_caching(schema_relation) %}
  {#-- Spark with iceberg tables don't work with show table extended for #}
  {#-- V2 iceberg tables #}
  {#-- https://issues.apache.org/jira/browse/SPARK-33393 #}
  {% call statement('list_relations_without_caching_show_tables', fetch_result=True) -%}
    show tables in {{ schema_relation.schema }} like '{{ schema_relation.identifier or "*" }}'
  {% endcall %}

  {% do return(load_result('list_relations_without_caching_show_tables').table) %}
{% endmacro %}

{% macro describe_table_extended_without_caching(table_name) %}
  {#-- Spark with iceberg tables don't work with show table extended for #}
  {#-- V2 iceberg tables #}
  {#-- https://issues.apache.org/jira/browse/SPARK-33393 #}
  {% call statement('describe_table_extended_without_caching', fetch_result=True) -%}
    describe extended {{ table_name }}
  {% endcall %}
  {% do return(load_result('describe_table_extended_without_caching').table) %}
{% endmacro %}

-- override macro to list only schemas related to current dbt project
{% macro spark__list_schemas(database) -%}
  {% call statement('list_schemas', fetch_result=True, auto_begin=False) %}
    show databases like '{{ database or "*" }}'
  {% endcall %}
  {{ return(load_result('list_schemas').table) }}
{% endmacro %}

{% macro spark__rename_relation(from_relation, to_relation) -%}
  {% call statement('rename_relation') -%}
    {% if not from_relation.type %}
      {% do exceptions.raise_database_error("Cannot rename a relation with a blank type: " ~ from_relation.identifier) %}
    {% elif from_relation.type in ('table') %}
        alter table {{ from_relation }} rename to {{ to_relation }}
    {% elif from_relation.type == 'view' %}
        alter view {{ from_relation }} rename to {{ to_relation }}
    {% else %}
      {% do exceptions.raise_database_error("Unknown type '" ~ from_relation.type ~ "' for relation: " ~ from_relation.identifier) %}
    {% endif %}
  {%- endcall %}
{% endmacro %}

{% macro spark__drop_relation(relation) -%}
  {% call statement('drop_relation', auto_begin=False) -%}
    drop {{ relation.type }} if exists {{ relation }}
  {%- endcall %}
{% endmacro %}


{% macro spark__generate_database_name(custom_database_name=none, node=none) -%}
  {% do return(None) %}
{%- endmacro %}

{% macro spark__persist_docs(relation, model, for_relation, for_columns) -%}
  {%- set raw_persist_docs = config.get('persist_docs', {}) -%}

  {%- if raw_persist_docs is mapping -%}
    {%- set raw_columns = raw_persist_docs.get('columns', true) -%}
    {%- set raw_relation = raw_persist_docs.get('relation', true) -%}
      {%- if for_columns and raw_columns and model.columns -%}
        {% do alter_column_comment(relation, model.columns) %}
      {% endif %}
      {%- if for_relation and raw_relation -%}
         {% do alter_relation_comment(relation, model.description) %}
      {% endif %}
  {%- elif raw_persist_docs -%}
        {{ exceptions.raise_compiler_error("Invalid value provided for 'persist_docs'. Expected dict but got value: " ~ raw_persist_docs) }}
  {% endif %}
{% endmacro %}

{% macro spark__alter_column_comment(relation, column_dict) %}
  {%- set file_format = config.get('file_format', default='openhouse') -%}
  {% if file_format in ['delta', 'hudi', 'iceberg', 'openhouse'] %}
    {% for column_name in column_dict %}
      {% set comment = column_dict[column_name]['description'] %}
      {% set escaped_comment = comment | replace('\'', '\\\'') %}
      {% set comment_query %}
        {% if relation.is_iceberg or relation.is_openhouse %}
          alter table {{ relation }} alter column
              {{ adapter.quote(column_name) if column_dict[column_name]['quote'] else column_name }}
              comment '{{ escaped_comment }}';
        {% else %}
          alter table {{ relation }} change column
              {{ adapter.quote(column_name) if column_dict[column_name]['quote'] else column_name }}
              comment '{{ escaped_comment }}';
        {% endif %}
      {% endset %}
      {% do run_query(comment_query) %}
    {% endfor %}
  {% endif %}
{% endmacro %}

{% macro spark__alter_relation_comment(relation, relation_comment) %}
  {% if config.get('file_format', default='openhouse') in ['openhouse'] %}
    {% set escaped_comment = relation_comment | replace('\'', '\\\'') %}
    {% set comment_query %}
        {% if escaped_comment|length %}
            alter table {{ relation }} set tblproperties ('comment'='{{ escaped_comment }}');
        {% else %}
            alter table {{ relation }} unset tblproperties ('comment');
        {% endif %}
    {% endset %}
    {% do run_query(comment_query) %}
  {% endif %}
{% endmacro %}

{% macro spark__make_temp_relation(base_relation, suffix) %}
    {% set tmp_identifier = base_relation.identifier ~ suffix %}
    {% set tmp_relation = base_relation.incorporate(path = {
        "identifier": tmp_identifier
    }) -%}

    {% do return(tmp_relation) %}
{% endmacro %}


{% macro spark__alter_column_type(relation, column_name, new_column_type) -%}
  {% call statement('alter_column_type') %}
    alter table {{ relation }} alter column {{ column_name }} type {{ new_column_type }};
  {% endcall %}
{% endmacro %}


{% macro spark__alter_relation_add_remove_columns(relation, add_columns, remove_columns) %}

  {% if remove_columns %}
    {% if relation.is_delta %}
      {% set platform_name = 'Delta Lake' %}
    {% elif relation.is_iceberg %}
      {% set platform_name = 'Iceberg' %}
    {% elif relation.is_openhouse %}
      {% set platform_name = 'OpenHouse' %}
    {% else %}
      {% set platform_name = 'Apache Spark' %}
    {% endif %}
    {{ exceptions.raise_compiler_error(platform_name + ' does not support dropping columns from tables') }}
  {% endif %}

  {% if add_columns is none %}
    {% set add_columns = [] %}
  {% endif %}

  {% set sql -%}

     alter {{ relation.type }} {{ relation }}

       {% if add_columns %} add columns {% endif %}
            {% for column in add_columns %}
               {{ column.name }} {{ column.data_type }}{{ ',' if not loop.last }}
            {% endfor %}

  {%- endset -%}

  {% do run_query(sql) %}

{% endmacro %}

{% macro spark__get_binding_char() %}
  {{ return('?' if target.method == 'odbc' else '%s') }}
{% endmacro %}


{% macro spark__reset_csv_table(model, full_refresh, old_relation, agate_table) %}
    {% if old_relation %}
        {{ adapter.drop_relation(old_relation) }}
    {% endif %}
    {% set sql = create_csv_table(model, agate_table) %}
    {{ return(sql) }}
{% endmacro %}


{% macro spark__load_csv_rows(model, agate_table) %}

  {% set batch_size = get_batch_size() %}
  {% set column_override = model['config'].get('column_types', {}) %}

  {% set statements = [] %}

  {% for chunk in agate_table.rows | batch(batch_size) %}
      {% set bindings = [] %}

      {% for row in chunk %}
          {% do bindings.extend(row) %}
      {% endfor %}

      {% set sql %}
          insert into {{ this.render() }} values
          {% for row in chunk -%}
              ({%- for col_name in agate_table.column_names -%}
                  {%- set inferred_type = adapter.convert_type(agate_table, loop.index0) -%}
                  {%- set type = column_override.get(col_name, inferred_type) -%}
                    {# todo- https://jira01.corp.linkedin.com:8443/browse/DATAFND-660 #}
                    cast('{{ row.get(col_name) if row.get(col_name) is not none else null }}' as {{type}})
                  {%- if not loop.last%},{%- endif %}
              {%- endfor -%})
              {%- if not loop.last%},{%- endif %}
          {%- endfor %}
      {% endset %}

      {% do adapter.add_query(sql, bindings=bindings, abridge_sql_log=True) %}

      {% if loop.index0 == 0 %}
          {% do statements.append(sql) %}
      {% endif %}
  {% endfor %}

  {# Return SQL so we can render it out into the compiled files #}
  {{ return(statements[0]) }}
{% endmacro %}


{% macro spark__create_csv_table(model, agate_table) %}
  {%- set column_override = model['config'].get('column_types', {}) -%}
  {%- set quote_seed_column = model['config'].get('quote_columns', None) -%}

  {% set sql %}
    create table {{ this.render() }} (
        {%- for col_name in agate_table.column_names -%}
            {%- set inferred_type = adapter.convert_type(agate_table, loop.index0) -%}
            {%- set type = column_override.get(col_name, inferred_type) -%}
            {%- set column_name = (col_name | string) -%}
            {{ adapter.quote_seed_column(column_name, quote_seed_column) }} {{ type }} {%- if not loop.last -%}, {%- endif -%}
        {%- endfor -%}
    )
    {{ file_format_clause() }}
    {{ partition_cols(label="partitioned by") }}
    {{ clustered_cols(label="clustered by") }}
    {{ location_clause() }}
    {{ comment_clause() }}
  {% endset %}

  {% call statement('_') -%}
    {{ sql }}
  {%- endcall %}

  {{ return(sql) }}
{% endmacro %}
