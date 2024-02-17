; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

@0 = internal constant [5 x i8] c"Tag0\00"
@1 = internal constant [5 x i8] c"Tag1\00"
@2 = internal constant [5 x i8] c"Tag2\00"

define void @signed_cmp_test() local_unnamed_addr #0 {
entry:
  %0 = add i64 2, 1
  %1 = add i64 %0, -1
  %2 = add i64 -1, %0
  %3 = sub i64 %0, -1
  call void @__quantum__rt__int_record_output(i64 %1, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %2, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @1, i32 0, i32 0))
  call void @__quantum__rt__int_record_output(i64 %3, i8* getelementptr inbounds ([5 x i8], [5 x i8]* @2, i32 0, i32 0))
  ret void
}

declare void @__quantum__rt__int_record_output(i64, i8*)

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
